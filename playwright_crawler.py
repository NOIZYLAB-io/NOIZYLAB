import os
import queue
import subprocess
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.robotparser import RobotFileParser
from typing import Coroutine, Callable, Any, Coroutine
import sys

import markdownify
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, Browser, Page
from asyncio import Queue, Lock, Semaphore
import asyncio
from overrides import override
from BASE.utils.path_selector import PathSelector

from logger.log import logger, LogDB, trace_context, set_trace_id, clear_trace_id

# Constants for optimization
DEFAULT_MAX_WORKERS = max(
    4, min(int(os.cpu_count() * 0.75), 8)
)  # Use 75% of CPU cores, capped at 8
DEFAULT_TIMEOUT = 30000  # 30 seconds
DEFAULT_WAIT_TIME = 1000  # 1 second
MAX_CONCURRENT_PAGES = 3  # Max concurrent pages per browser context

@logger.catch()
class PlaywrightCrawlerBackend():
    """
    A web crawler backend that uses Playwright for rendering JavaScript-heavy sites.
    """

    def __init__(self, max_pages: int = 500, max_depth: int = 10):
        """
        Initialize the Playwright crawler backend.

        Args:
            max_pages: Maximum number of pages to scrape (default: 500)
            max_workers: Maximum number of concurrent workers (default: DEFAULT_MAX_WORKERS)
            max_depth: Maximum crawling depth (default: 10)
        """
        self.max_pages = max_pages
        self.max_workers = DEFAULT_MAX_WORKERS
        self.max_depth = max_depth
        logger.info(
            f"Initialized crawler with max_pages={max_pages}, max_workers={self.max_workers}, max_depth={max_depth}"
        )

    async def _install_dependencies(self) -> None:
        """Install Playwright browser dependencies (internal method)."""
        logger.info("Installing Playwright dependencies...")
        env = os.environ.copy()
        try:
            subprocess.run(
                ["playwright", "install", "chromium"],
                env=env,
                shell=False,
            )
            logger.info("Successfully installed Playwright dependencies")
        except Exception as e:
            logger.error(f"Failed to install Playwright dependencies: {e}")
            raise

    def _is_same_domain_or_subdomain(self, url1: str, url2: str) -> bool:
        """
        Check if two URLs belong to the same domain or subdomain.

        Args:
            url1: First URL to compare
            url2: Second URL to compare

        Returns:
            True if URLs are from same domain/subdomain, False otherwise
        """
        parsed1 = urlparse(url1)
        parsed2 = urlparse(url2)

        # Handle relative URLs
        if parsed1.netloc == "":
            return True

        # Split domains into parts
        domain1_parts = parsed1.netloc.split(".")
        domain2_parts = parsed2.netloc.split(".")

        # Compare root domain and TLD (last two parts)
        if len(domain1_parts) >= 2 and len(domain2_parts) >= 2:
            return domain1_parts[-2:] == domain2_parts[-2:]

        return parsed1.netloc == parsed2.netloc

    async def _collect_urls(self, start_url: str) -> set[str]:
        """
        First phase: Collect all unique URLs from the site up to max_pages.
        Uses multiple browser contexts for parallel processing.
        """
        start_time = time.time()
        logger.info(f"Starting URL collection from: {start_url}")

        urls_to_scrape = set()
        urls_to_scrape.add(start_url)

        urls_to_visit = Queue()
        await urls_to_visit.put((start_url, 0))  # (url, depth)

        visited = set()
        visited_lock = Lock()
        page_semaphore = Semaphore(MAX_CONCURRENT_PAGES)

        async def process_url(browser: Browser, url: str, depth: int):
            async with page_semaphore:  # Limit concurrent pages
                try:
                    context = await browser.new_context(
                        viewport={'width': 1920, 'height': 1080},
                        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                        java_script_enabled=False,
                        bypass_csp=True,
                        ignore_https_errors=True
                    )
                    page = await context.new_page()

                    logger.debug(f"Collecting links from: {url} (depth: {depth})")

                    await page.goto(
                        url, timeout=DEFAULT_TIMEOUT, wait_until="networkidle"
                    )
                    await page.wait_for_timeout(DEFAULT_WAIT_TIME)

                    html_content = await page.content()
                    await page.close()
                    await context.close()

                    soup = BeautifulSoup(html_content, "html.parser")
                    links_found = 0

                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        next_url = urljoin(url, href)
                        next_url = urldefrag(next_url)[0]

                        if self._is_same_domain_or_subdomain(next_url, start_url):
                            async with visited_lock:
                                if (
                                    next_url not in urls_to_scrape
                                    and len(urls_to_scrape) < self.max_pages
                                ):
                                    urls_to_scrape.add(next_url)
                                    if depth < self.max_depth:
                                        await urls_to_visit.put((next_url, depth + 1))
                                    links_found += 1

                    logger.info(
                        f"Found {links_found} new links on {url} (Total unique URLs: {len(urls_to_scrape)})"
                    )

                except Exception as e:
                    logger.error(f"Error collecting URLs from {url}: {e}")

        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=True,
                    args=[
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-dev-shm-usage',
                        '--disable-accelerated-2d-canvas',
                        '--no-first-run',
                        '--no-zygote',
                        '--disable-gpu',
                        '--disable-background-timer-throttling',
                        '--disable-backgrounding-occluded-windows',
                        '--disable-renderer-backgrounding',
                        '--disable-features=TranslateUI',
                        '--disable-ipc-flooding-protection',
                        '--disable-default-apps',
                        '--disable-extensions',
                        '--disable-plugins',
                        '--disable-images',
                        '--disable-javascript',
                        '--disable-web-security',
                        '--disable-features=VizDisplayCompositor',
                        '--disable-background-networking',
                        '--disable-sync',
                        '--disable-translate',
                        '--hide-scrollbars',
                        '--mute-audio',
                        '--no-default-browser-check',
                        '--safebrowsing-disable-auto-update',
                        '--disable-client-side-phishing-detection',
                        '--disable-component-update',
                        '--disable-domain-reliability',
                        '--disable-features=AudioServiceOutOfProcess',
                        '--disable-hang-monitor',
                        '--disable-prompt-on-repost',
                        '--disable-background-media-suspend',
                        '--disable-component-extensions-with-background-pages',
                        '--disable-features=TranslateUI,BlinkGenPropertyTrees',
                        '--disable-ipc-flooding-protection',
                        '--disable-renderer-backgrounding',
                        '--enable-features=NetworkService,NetworkServiceLogging',
                        '--force-color-profile=srgb',
                        '--metrics-recording-only',
                        '--no-default-browser-check',
                        '--no-first-run',
                        '--password-store=basic',
                        '--use-mock-keychain',
                        '--disable-blink-features=AutomationControlled'
                    ]
                )

                tasks = []
                while (
                    not urls_to_visit.empty() and len(urls_to_scrape) < self.max_pages
                ):
                    current_url, depth = await urls_to_visit.get()

                    async with visited_lock:
                        if current_url in visited:
                            continue
                        visited.add(current_url)

                    if depth <= self.max_depth:
                        task = asyncio.create_task(
                            process_url(browser, current_url, depth)
                        )
                        tasks.append(task)

                        # Process in batches to control memory usage
                        if len(tasks) >= self.max_workers:
                            await asyncio.gather(*tasks)
                            tasks = []

                if tasks:
                    await asyncio.gather(*tasks)

                await browser.close()

        except Exception as e:
            logger.error(f"Error during URL collection: {e}")
            raise



        return urls_to_scrape

    async def _scrape_url(self, url: str, browser: Browser):
        logger.info(f"Scraping URL: {url}")

        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            java_script_enabled=False,
            bypass_csp=True,
            ignore_https_errors=True
        )

        retries = 5
        while retries > 0:
            try:
                logger.debug(f"Scraping content from: {url}")
                page = await context.new_page()
                await page.goto(
                    url,
                    timeout=DEFAULT_TIMEOUT,
                    wait_until="networkidle",
                )
                await page.wait_for_timeout(DEFAULT_WAIT_TIME)

                html_content = await page.content()
                await page.close()

                soup = BeautifulSoup(html_content, "html.parser")

                if soup.footer:
                    soup.footer.decompose()

                for tag_name in [
                    "canvas",
                    "img",
                    "video",
                    "audio",
                    "style",
                    "script",
                    "form",
                    "button",
                ]:
                    for tag in soup.find_all(tag_name):
                        tag.decompose()

                body = soup.body
                if not body:
                    raise ValueError(f"No body found for {url}")
                return markdownify.markdownify(str(body), heading_style="ATX")
            except Exception as e:
                logger.error(f"Error scraping {url}: {e}")
                retries -= 1
                await asyncio.sleep(1)

        await context.close()
        raise ValueError(f"Failed to scrape {url} after {5 - retries} retries")

    async def _scrape_urls(
        self,
        urls: list[str],
        progress_callback: Callable[[float], Coroutine[Any, Any, Any]],
    ) -> dict[str, str]:
        """
        Second phase: Scrape content from collected URLs.
        Uses multiple browser instances for true parallel processing.
        """

        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-accelerated-2d-canvas',
                    '--no-first-run',
                    '--no-zygote',
                    '--disable-gpu',
                    '--disable-background-timer-throttling',
                    '--disable-backgrounding-occluded-windows',
                    '--disable-renderer-backgrounding',
                    '--disable-features=TranslateUI',
                    '--disable-ipc-flooding-protection',
                    '--disable-default-apps',
                    '--disable-extensions',
                    '--disable-plugins',
                    '--disable-images',
                    '--disable-javascript',
                    '--disable-web-security',
                    '--disable-features=VizDisplayCompositor',
                    '--disable-background-networking',
                    '--disable-sync',
                    '--disable-translate',
                    '--hide-scrollbars',
                    '--mute-audio',
                    '--no-default-browser-check',
                    '--safebrowsing-disable-auto-update',
                    '--disable-client-side-phishing-detection',
                    '--disable-component-update',
                    '--disable-domain-reliability',
                    '--disable-features=AudioServiceOutOfProcess',
                    '--disable-hang-monitor',
                    '--disable-prompt-on-repost',
                    '--disable-background-media-suspend',
                    '--disable-component-extensions-with-background-pages',
                    '--disable-features=TranslateUI,BlinkGenPropertyTrees',
                    '--disable-ipc-flooding-protection',
                    '--disable-renderer-backgrounding',
                    '--enable-features=NetworkService,NetworkServiceLogging',
                    '--force-color-profile=srgb',
                    '--metrics-recording-only',
                    '--no-default-browser-check',
                    '--no-first-run',
                    '--password-store=basic',
                    '--use-mock-keychain',
                    '--disable-blink-features=AutomationControlled'
                ]
            )

            processed_count = 0
            total_count = len(urls)

            async def _scrape_batch(urls: list[str]) -> dict[str, str]:
                nonlocal processed_count

                async def _scrape_url(url: str) -> str:
                    nonlocal processed_count
                    result = await self._scrape_url(url, browser)
                    processed_count += 1
                    logger.info(f"Scraped {processed_count}/{total_count} URLs")
                    if progress_callback:
                        await progress_callback(processed_count / total_count * 100)
                    return result

                logger.info(f"Scraping {len(urls)} URLs in batch ({' '.join(urls)})")
                futures = []
                for url in urls:
                    futures.append(asyncio.create_task(_scrape_url(url)))
                results = await asyncio.gather(*futures, return_exceptions=True)
                safe_results = {}
                for url, result in zip(urls, results):
                    if isinstance(result, Exception):
                        safe_results[url] = f"Error: {str(result)}"
                    else:
                        safe_results[url] = result
                return safe_results

            final_result: dict[str, str] = {}
            for i in range(0, len(urls), self.max_workers):
                batch_urls = urls[i : i + self.max_workers]
                results = await _scrape_batch(batch_urls)
                final_result.update(results)

            logger.info(f"Scraped {len(final_result)} URLs: {final_result.items()}")

            await browser.close()

        return final_result

    async def scrape(
        self,
        url: str,
        progress_callback: Callable[[float], Coroutine[Any, Any, Any]] | None = None,
    ) -> Coroutine[dict[str, str], None, None]:
        """
        Scrape a website starting from url and save content to path.
        Uses a two-phase approach:
        1. Collect all unique URLs up to max_pages
        2. Scrape content from collected URLs

        Args:
            url: The URL to start crawling from

        Returns:
            dict of {url: content}
        """
        start_time = time.time()
        logger.info(f"Starting scraping process for {url}")

        if progress_callback:
            await progress_callback(1)

        try:
            # set up the custom browser binaries directory
            browsers_path = os.path.abspath(
                os.path.join(PathSelector.get_qdrant_db_path(), "browser_binaries")
            )
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browsers_path

            # Phase 1: Collect URLs
            logger.info("\nPhase 1: Collecting URLs...")
            urls_to_scrape = await self._collect_urls(url)
            logger.info(f"Found {len(urls_to_scrape)} unique URLs to scrape")

            # Phase 2: Scrape Content
            logger.info("\nPhase 2: Scraping content...")
            scraped_contents = await self._scrape_urls(
                list(urls_to_scrape), progress_callback
            )
            logger.info(f"Scraped {len(scraped_contents)} URLs")

            return scraped_contents
        except Exception as e:
            logger.error(f"Scraping failed: {e}")
            raise

    def _get_file_path(self, url: str) -> str:
        """
        Generate a file path for the given URL.

        Args:
            url: The URL to generate a file path for

        Returns:
            A relative file path for saving the content
        """
        relative_path = urlparse(url).path
        if relative_path == "":
            relative_path = "/index.md"
        elif relative_path.endswith("/"):
            relative_path += "index.md"
        else:
            # Replace .html or .htm extension with .md
            if relative_path.endswith(".html") or relative_path.endswith(".htm"):
                relative_path = relative_path.rsplit(".", 1)[0] + ".md"
            else:
                relative_path += ".md"
        if relative_path.startswith("/"):
            relative_path = relative_path[1:]
        return relative_path
