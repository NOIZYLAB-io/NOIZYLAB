# Standalone Playwright Crawler

This directory contains a standalone Playwright web crawler that can be run as a separate Python process, allowing for better isolation and resource management.

## Files

- `playwright_crawler.py` - Original Playwright crawler class
- `playwright_crawler_script.py` - Standalone script that can be run as a separate process
- `docs.py` - Modified to call the standalone script instead of importing the class directly

## Usage

### Running the Standalone Script

The `playwright_crawler_script.py` can be run directly from the command line:

```bash
python BASE/chunkers/playwright_crawler_script.py [OPTIONS] URL1 URL2 URL3...
```

#### Options

- `--max-pages INT`: Maximum pages to scrape per URL (default: 100)
- `--max-depth INT`: Maximum crawling depth per URL (default: 10)
- `--output FILE` or `-o FILE`: Output file path (default: stdout)

#### Examples

```bash
# Scrape a single URL and output to stdout
python BASE/chunkers/playwright_crawler_script.py https://example.com

# Scrape multiple URLs with custom limits
python BASE/chunkers/playwright_crawler_script.py --max-pages 50 --max-depth 5 https://example.com https://example.org

# Save results to a file
python BASE/chunkers/playwright_crawler_script.py -o results.json https://example.com
```

### Output Format

The script outputs JSON in the following format:

```json
{
  "https://example.com": {
    "status": "success",
    "content": {
      "https://example.com/page1": "scraped content...",
      "https://example.com/page2": "scraped content..."
    },
    "pages_scraped": 2
  },
  "https://example.org": {
    "status": "error",
    "error": "Connection timeout",
    "content": {}
  }
}
```

### Integration with docs.py

The `docs.py` module has been modified to call the standalone script instead of importing the Playwright class directly. This provides:

1. **Process Isolation**: The crawler runs in a separate process, preventing memory leaks and crashes from affecting the main application
2. **Resource Management**: Better control over system resources
3. **Error Handling**: Improved error isolation and recovery
4. **Scalability**: Easier to scale by running multiple instances

## Testing

Use the test script to verify the standalone crawler works:

```bash
python test_playwright_script.py
```

## Benefits of the New Approach

1. **Separation of Concerns**: The crawler logic is completely separate from the docs processing
2. **Process Isolation**: Memory leaks or crashes in the crawler won't affect the main application
3. **Better Error Handling**: Each process can handle its own errors independently
4. **Resource Management**: Easier to control and monitor resource usage
5. **Scalability**: Can easily run multiple crawler instances in parallel
6. **Debugging**: Easier to debug issues as they're isolated to specific processes

## Requirements

- Python 3.7+
- Playwright (`pip install playwright`)
- Playwright browsers (`playwright install chromium`)
- All other dependencies from the original project

## Troubleshooting

### Common Issues

1. **Playwright not installed**: Run `pip install playwright && playwright install chromium`
2. **Permission errors**: Ensure the script has execute permissions
3. **Path issues**: Make sure the script path is correct when called from docs.py
4. **Timeout errors**: Increase the timeout in docs.py if scraping takes longer than expected

### Debug Mode

To run the crawler script with more verbose output, you can modify the logging level in the script or add debug prints as needed.









