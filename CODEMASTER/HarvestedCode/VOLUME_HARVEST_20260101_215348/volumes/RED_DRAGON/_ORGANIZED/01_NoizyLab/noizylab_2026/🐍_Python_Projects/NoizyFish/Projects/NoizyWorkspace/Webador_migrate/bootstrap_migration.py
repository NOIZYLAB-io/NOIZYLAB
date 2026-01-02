#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bootstrap the Webador → GoDaddy migration toolkit.

What this does:
- Creates project structure
- Writes a full-featured migration script: migrate.py
  - --transfer   : log into Webador via Selenium, try to capture EPP/Auth code (manual fallback)
  - --archive    : crawl live site, save pages/images/css/js, build sitemap
  - --all        : does both, in order
- Creates .vscode/tasks.json + keybindings.json + launch.json
- Creates requirements.txt, Makefile, README.md checklists
- Creates output/ for results and logs
- Optionally sets up a Python venv and installs deps (prompt)

After running, open folder in VS Code and use the tasks to execute.

Notes:
- We intentionally keep Webador login flexible (selectors vary). If EPP isn't visible,
  the script opens the dashboard and prompts you to complete the step manually, then paste the code.
- Never paste credentials into this file; pass via environment variables when running migrate.py:
    export WEBADOR_EMAIL="you@example.com"
    export WEBADOR_PASS="yourPassword"
    export WEBADOR_SITE_URL="https://YOUR-LIVE-SITE.TLD"   # for archiving
"""

import os
import sys
import textwrap
from pathlib import Path
from datetime import datetime
import yaml

ROOT = Path.cwd()
VSC = ROOT / ".vscode"
OUTPUT = ROOT / "output"
TOOLS = ROOT / "tools"

def w(path: Path, content: str, exist_ok=True):
    path.parent.mkdir(parents=True, exist_ok=True)
    if (not path.exists()) or exist_ok:
        path.write_text(content, encoding="utf-8")

def load_config():
    config_path = ROOT / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def main():
    print(f"Bootstrap in: {ROOT}")
    (ROOT / "scripts").mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    TOOLS.mkdir(parents=True, exist_ok=True)
    VSC.mkdir(parents=True, exist_ok=True)

    # ---------------------- migrate.py ----------------------
    migrate_py = textwrap.dedent(r'''
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Webador → GoDaddy Migration Tool

    Modes:
      --transfer    Attempt to capture EPP/Auth code from Webador (manual fallback)
      --archive     Crawl live site (HTML, images, css, js) into output/
      --all         Do both, transfer then archive

    ENV VARS:
      WEBADOR_EMAIL, WEBADOR_PASS  : for login
      OUTPUT_DIR                   : where to write outputs (default: ./output)
      WEBADOR_SITE_URL             : live site root URL to crawl (e.g., https://example.com)

    Dependencies:
      selenium, webdriver-manager, requests, beautifulsoup4, lxml, tldextract, tqdm

    Usage:
      export WEBADOR_EMAIL="you@example.com"
      export WEBADOR_PASS="yourPassword"
      export WEBADOR_SITE_URL="https://your-live-site.tld"
      python3 migrate.py --all
    """

    import os
    import sys
    import re
    import json
    import time
    import getpass
    import traceback
    from pathlib import Path
    from urllib.parse import urljoin, urlparse
    import webbrowser

    import requests
    from bs4 import BeautifulSoup
    from tqdm import tqdm
    import tldextract

    # Selenium (login / EPP)
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException, WebDriverException

    DEFAULT_OUTPUT = Path(os.getenv("OUTPUT_DIR", str(Path.cwd() / "output"))).expanduser()
    DEFAULT_OUTPUT.mkdir(parents=True, exist_ok=True)
    LOG_FILE = DEFAULT_OUTPUT / "status.log"
    EPP_FILE = DEFAULT_OUTPUT / "transfer_codes.json"
    SITEMAP_FILE = DEFAULT_OUTPUT / "sitemap.txt"

    def log(msg: str):
        line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n"
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(line)
        print(msg)

    def save_json(path: Path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def read_env(name: str, prompt: str = None, secret=False):
        val = os.getenv(name)
        if val:
            return val
        if prompt:
            return getpass.getpass(prompt + ": ") if secret else input(prompt + ": ")
        return None

    # --------------------- TRANSFER (EPP) ---------------------
    def fetch_epp_code():
        email = read_env("WEBADOR_EMAIL", "WEBADOR_EMAIL", secret=False)
        password = read_env("WEBADOR_PASS", "WEBADOR_PASS", secret=True)
        if not email or not password:
            log("Missing WEBADOR_EMAIL or WEBADOR_PASS; cannot continue EPP automation.")
            return None

        webador_login_url = "https://www.webador.com/v2/dashboard"
        epp_code = None
        notes = []

        try:
            log("Launching Chrome via webdriver_manager…")
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

            driver.get(webador_login_url)
            time.sleep(2)

            # Try common login field patterns
            def try_login():
                nonlocal epp_code
                try:
                    email_field = None
                    pass_field = None
                    # try by name first
                    for sel in ["input[type='email']", "input[name='email']", "#email"]:
                        try:
                            email_field = driver.find_element(By.CSS_SELECTOR, sel)
                            break
                        except Exception:
                            pass
                    for sel in ["input[type='password']", "input[name='password']", "#password"]:
                        try:
                            pass_field = driver.find_element(By.CSS_SELECTOR, sel)
                            break
                        except Exception:
                            pass
                    if email_field and pass_field:
                        email_field.clear(); email_field.send_keys(email)
                        pass_field.clear(); pass_field.send_keys(password)
                        pass_field.send_keys(Keys.RETURN)
                        time.sleep(4)
                        return True
                    return False
                except Exception:
                    return False

            if not try_login():
                log("Could not auto-fill login; please complete login manually in the opened browser, then press Enter here.")
                input("Press Enter after you're logged in…")

            time.sleep(3)
            log(f"Post-login URL: {driver.current_url}")

            # Try to reach domain settings
            def click_possible_domain_links():
                candidates = [
                    "//a[contains(translate(., 'DOMAIN', 'domain'),'domain')]",
                    "//a[contains(translate(., 'DOMAINS', 'domains'),'domains')]",
                    "//button[contains(translate(., 'DOMAIN', 'domain'),'domain')]",
                    "//a[contains(@href,'domain')]",
                ]
                for xp in candidates:
                    try:
                        el = driver.find_element(By.XPATH, xp)
                        el.click()
                        time.sleep(2)
                        return True
                    except Exception:
                        pass
                return False

            if not click_possible_domain_links():
                # try common path guesses
                guesses = [
                    "https://www.webador.com/v2/dashboard/domains",
                    "https://www.webador.com/domains",
                    "https://www.webador.com/v2/dashboard/domain",
                ]
                for g in guesses:
                    try:
                        driver.get(g)
                        time.sleep(2)
                        if "domain" in driver.page_source.lower():
                            break
                    except Exception:
                        pass

            # Attempt to regex an EPP/Auth code from page
            page = driver.page_source
            m = re.search(r"(EPP|Auth(orization)?|Transfer)\s*code[^A-Za-z0-9\-]*([A-Za-z0-9\-]{6,})", page, re.IGNORECASE)
            if m:
                epp_code = m.group(3).strip()
                notes.append("EPP found via regex.")
            else:
                # maybe a "reveal" button is present
                try:
                    btn = driver.find_element(By.XPATH, "//button[contains(.,'EPP') or contains(.,'Auth') or contains(.,'Transfer')]")
                    btn.click()
                    time.sleep(2)
                    page = driver.page_source
                    m = re.search(r"([A-Za-z0-9\-]{6,})", page)
                    if m:
                        epp_code = m.group(1).strip()
                        notes.append("EPP found after reveal click.")
                except Exception:
                    pass

            if not epp_code:
                log("Could not auto-detect EPP code. If Webador sent it by email, paste it below.")
                pasted = input("Paste EPP/Auth code (or press Enter to skip): ").strip()
                if pasted:
                    epp_code = pasted
                    notes.append("EPP provided manually by user.")
                else:
                    notes.append("EPP not found.")

            try:
                driver.quit()
            except Exception:
                pass

        except WebDriverException as e:
            log(f"Selenium/WebDriver error: {e}")
        except Exception as e:
            log(f"Unexpected error during transfer step: {e}\n{traceback.format_exc()}")

        if epp_code:
            rec = {
                "timestamp": int(time.time()),
                "epp_code": epp_code,
                "notes": notes
            }
            # append to JSON list
            existing = []
            if EPP_FILE.exists():
                try:
                    existing = json.loads(EPP_FILE.read_text(encoding="utf-8"))
                    if not isinstance(existing, list):
                        existing = [existing]
                except Exception:
                    existing = []
            existing.append(rec)
            save_json(EPP_FILE, existing)
            log(f"Saved EPP to {EPP_FILE}")
        else:
            log("No EPP code saved.")
        return epp_code

    # ---------------------- ARCHIVE (CRAWL) ----------------------
    def normalize_url(u: str):
        return u.split("#")[0]

    def same_site(root, url):
        # allow subpaths and same registered domain
        e1 = tldextract.extract(root)
        e2 = tldextract.extract(url)
        return (e1.registered_domain == e2.registered_domain)

    def archive_site():
        root = os.getenv("WEBADOR_SITE_URL")
        if not root:
            root = input("Enter live site URL to archive (e.g., https://example.com): ").strip()
        if not root:
            log("Archive canceled: missing site URL.")
            return

        session = requests.Session()
        visited = set()
        queue = [root]
        pages_dir = DEFAULT_OUTPUT / "site" / "pages"
        assets_img = DEFAULT_OUTPUT / "site" / "images"
        assets_css = DEFAULT_OUTPUT / "site" / "css"
        assets_js  = DEFAULT_OUTPUT / "site" / "js"
        for d in (pages_dir, assets_img, assets_css, assets_js):
            d.mkdir(parents=True, exist_ok=True)

        discovered_urls = []

        def save_asset(url: str, dest_dir: Path):
            try:
                r = session.get(url, timeout=20, stream=True)
                if r.status_code == 200:
                    filename = Path(urlparse(url).path).name or "index"
                    dest = dest_dir / filename
                    with open(dest, "wb") as f:
                        for chunk in r.iter_content(8192):
                            f.write(chunk)
                    return True
            except Exception:
                pass
            return False

        log(f"Starting crawl: {root}")
        with open(SITEMAP_FILE, "w", encoding="utf-8") as sm:
            while queue:
                url = queue.pop(0)
                url = normalize_url(url)
                if url in visited:
                    continue
                visited.add(url)

                # same site filter
                if not same_site(root, url):
                    continue

                try:
                    r = session.get(url, timeout=20)
                except Exception as e:
                    log(f"Fetch failed: {url} ({e})")
                    continue
                if r.status_code != 200 or "text/html" not in (r.headers.get("Content-Type","")):
                    continue

                soup = BeautifulSoup(r.text, "lxml")
                # Save page
                netloc = urlparse(url).netloc.replace(":", "_")
                path = urlparse(url).path
                if path.endswith("/") or path == "":
                    filename = "index.html"
                else:
                    filename = Path(path).name
                    if "." not in filename:
                        filename += ".html"
                page_folder = pages_dir / netloc / Path(path).parent.relative_to("/") if path else pages_dir / netloc
                page_folder.mkdir(parents=True, exist_ok=True)
                page_path = page_folder / filename
                page_path.write_text(r.text, encoding="utf-8")

                sm.write(url + "\n")
                discovered_urls.append(url)

                # enqueue links
                for a in soup.find_all("a", href=True):
                    href = a["href"].strip()
                    if href.startswith("mailto:") or href.startswith("tel:"):
                        continue
                    full = urljoin(url, href)
                    if full not in visited and same_site(root, full):
                        queue.append(full)

                # download images
                for img in soup.find_all("img", src=True):
                    full = urljoin(url, img["src"])
                    save_asset(full, assets_img)

                # download css
                for lk in soup.find_all("link", href=True):
                    if lk.get("rel") and "stylesheet" in [v.lower() for v in lk.get("rel")]:
                        full = urljoin(url, lk["href"])
                        save_asset(full, assets_css)

                # download js
                for sc in soup.find_all("script", src=True):
                    full = urljoin(url, sc["src"])
                    save_asset(full, assets_js)

        meta = {
            "root": root,
            "pages_count": len(discovered_urls),
            "output": str(DEFAULT_OUTPUT / "site"),
        }
        (DEFAULT_OUTPUT / "pages_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        log(f"Archive complete. {len(discovered_urls)} pages. See {DEFAULT_OUTPUT/'site'} and {SITEMAP_FILE}")

    # ---------------------- ENTRY ----------------------
    def run(mode: str):
        if mode == "--transfer":
            fetch_epp_code()
        elif mode == "--archive":
            archive_site()
        elif mode == "--all":
            code = fetch_epp_code()
            archive_site()
            if code:
                log("Next: Open GoDaddy transfer portal, paste EPP code, approve emails.")
                log("URL: https://dashboard.godaddy.com/venture?ventureId=02497ee5-490b-4e77-a207-f9e507a67a10")
        else:
            print(__doc__)

    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print(__doc__)
            sys.exit(0)
        run(sys.argv[1])
    ''')

    w(ROOT / "migrate.py", migrate_py)
    os.chmod(ROOT / "migrate.py", 0o755)

    # ---------------------- requirements.txt ----------------------
    reqs = """\
selenium
webdriver-manager
requests
beautifulsoup4
lxml
tldextract
tqdm
"""
    w(ROOT / "requirements.txt", reqs)

    # ---------------------- .vscode/tasks.json ----------------------
    tasks = {
      "version": "2.0.0",
      "tasks": [
        {
          "label": "Domain Transfer (EPP)",
          "type": "shell",
          "command": "python3 ${workspaceFolder}/migrate.py --transfer",
          "problemMatcher": []
        },
        {
          "label": "Content Archive (crawl)",
          "type": "shell",
          "command": "python3 ${workspaceFolder}/migrate.py --archive",
          "problemMatcher": []
        },
        {
          "label": "Run All (transfer + archive)",
          "type": "shell",
          "command": "python3 ${workspaceFolder}/migrate.py --all",
          "problemMatcher": []
        }
      ]
    }
    import json as _json
    w(VSC / "tasks.json", _json.dumps(tasks, indent=2))

    # ---------------------- .vscode/keybindings.json ----------------------
    keybindings = [
      { "key": "ctrl+alt+d", "command": "workbench.action.tasks.runTask", "args": "Domain Transfer (EPP)" },
      { "key": "ctrl+alt+c", "command": "workbench.action.tasks.runTask", "args": "Content Archive (crawl)" },
      { "key": "ctrl+alt+a", "command": "workbench.action.tasks.runTask", "args": "Run All (transfer + archive)" }
    ]
    w(VSC / "keybindings.json", _json.dumps(keybindings, indent=2))

    # ---------------------- .vscode/launch.json ----------------------
    launch = {
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Debug migrate.py (args in input box)",
          "type": "python",
          "request": "launch",
          "program": "${workspaceFolder}/migrate.py",
          "console": "integratedTerminal",
          "args": []
        }
      ]
    }
    w(VSC / "launch.json", _json.dumps(launch, indent=2))

    # ---------------------- Makefile ----------------------
    makefile = """\
.PHONY: venv deps transfer archive all

venv:
\tpython3 -m venv .venv

deps: venv
\t. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

transfer:
\tpython3 migrate.py --transfer

archive:
\tpython3 migrate.py --archive

all:
\tpython3 migrate.py --all
"""
    w(ROOT / "Makefile", makefile)

    # ---------------------- README.md ----------------------
    readme = f"""\
# Webador → GoDaddy Migration

**Folder:** `{ROOT}`

## Quick start
```bash
cd "{ROOT}"
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Environment
export WEBADOR_EMAIL="you@example.com"
export WEBADOR_PASS="yourPassword"
export WEBADOR_SITE_URL="https://YOUR-LIVE-SITE.TLD"

# Run all:
python3 migrate.py --all
```

## Manual setup (if needed)

If the automated setup did not work as expected, you can manually create the folder structure and files:

```bash
# Create the folder structure
mkdir -p ~/Desktop/NoizyFish/forward1/logs

# Create empty files (you can fill them in later)
touch ~/Desktop/NoizyFish/forward1/forward1.py
touch ~/Desktop/NoizyFish/forward1/config.yaml
touch ~/Desktop/NoizyFish/forward1/vault.key
touch ~/Desktop/NoizyFish/forward1/vault.enc
touch ~/Desktop/NoizyFish/forward1/logs/forward1.log
```
"""
    w(ROOT / "README.md", readme)

    # ---------------------- forward1.py ----------------------
    forward1_py = """\
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    print("Brand:", config["identity"]["brand"])
    print("Domains:")
    for domain in config["domains"]:
        print(f"  - {domain['name']} ({domain['status']})")
    # Add more automation here...

if __name__ == "__main__":
    main()
"""
    w(ROOT / "forward1.py", forward1_py)
    os.chmod(ROOT / "forward1.py", 0o755)

if __name__ == "__main__":
    main()