# Quicket Event Scraper

A Python web scraper that extracts event information from Quicket's events page using Selenium and BeautifulSoup4.

## Features

- Scrapes event titles, locations, dates, and times
- Supports both Firefox and Chrome browsers
- Headless mode for background operation
- Smooth scrolling simulation for natural behavior
- Progress tracking with page numbers
- Configurable scraping parameters
- CSV output with formatted data

## Requirements

- Python 3.6+
- Selenium
- BeautifulSoup4
- webdriver-manager
- Firefox or Chrome browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/consumin-helium/Web-Scraper.git
cd Web-Scraper
```

2. Activate the included virtual environment:
```bash
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

The virtual environment already includes all required packages:
- selenium
- beautifulsoup4
- webdriver-manager

If you prefer to create a fresh virtual environment instead:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
pip install selenium beautifulsoup4 webdriver-manager tqdm
```

1. Install browser driver (choose one):
   - Firefox (recommended): Will be installed automatically
   - Chrome: Will be installed automatically

## Configuration

Create a `config.py` file with your preferred settings:

```python
# Scraper Configuration
BROWSER = 'firefox'  # 'firefox' or 'chrome'
HEADLESS = True      # True for headless mode, False for GUI mode
NUM_PAGES = 2        # Number of pages to scrape
OUTPUT_FILE = 'quicket_events.csv'  # Output filename
```

## Usage

Run the scraper:
```bash
python scraper.py
```

The script will:
1. Launch a browser (headless by default)
2. Navigate to Quicket's events page
3. Scrape event information from specified number of pages
4. Save data to CSV file

## Output Format

The script generates a CSV file with the following columns:
- Event Title
- Event Location
- Event Date
- Event Time
- Page Number

## Customization

You can modify the scraping behavior by:
1. Editing `config.py` file
2. Passing parameters when calling the function:
```python
scrape_quicket_events(
    num_pages=5,
    output_filename='custom_output.csv',
    browser='chrome',
    headless=False
)
```

## Error Handling

The scraper includes robust error handling for:
- Network issues
- Missing elements
- Navigation errors
- Dynamic content loading

## Notes

- Use CSVLint in VS Code to align CSV whitespace if needed
- Delete the output CSV file to start fresh
- Adjust scroll delays in code if needed for slower connections
- Respects website's structure with appropriate delays

## Limitations

- Depends on Quicket's current HTML structure
- May need updates if website changes
- Requires stable internet connection
- Performance depends on system resources

## Author's Note

I loved this project! It was really fun getting back into web scraping as it took me to my roots. In fact, my current portfolio site lifts the contents of my works from Artstation using a selenium system such as this one. I hope you enjoy this project as much as I did!

### Challenges Overcome
- Handled dynamically loaded content using Selenium
- Implemented smooth scrolling for natural behavior
- Managed headless browser operations
- Structured data extraction with BeautifulSoup4

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.