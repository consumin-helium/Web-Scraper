# Scraper Configuration

# Browser settings
BROWSER = 'firefox'  # 'firefox' or 'chrome'
HEADLESS = True      # True for headless mode, False for GUI mode

# Scraping settings
NUM_PAGES = 10        # Number of pages to scrape
OUTPUT_FILE = 'quicket_events.csv'  # Output CSV filename

# Timing settings
PAGE_LOAD_WAIT = 10  # Seconds to wait for page elements to load
SCROLL_DELAY = 0.1   # Seconds between scroll steps
RANDOM_DELAY_MIN = 1 # Minimum seconds between pages
RANDOM_DELAY_MAX = 3 # Maximum seconds between pages