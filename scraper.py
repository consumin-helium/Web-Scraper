from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import csv
import time
import random

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import config


def setup_driver(browser='firefox', headless=True):
    """Setup and return a web driver instance."""
    if browser.lower() == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)


def scroll_to_bottom(driver):
    """Scroll to the bottom of the page smoothly"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down in smaller increments (100 pixels at a time)
        for i in range(0, last_height, 100):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1)  # Small delay for smooth scrolling
        
        # Wait for any dynamic content to load
        time.sleep(2)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_quicket_events(num_pages=None, output_filename=None, browser=None, headless=None):
    """
    Scrapes event data from Quicket's event pages using Selenium and BeautifulSoup.
    
    Args:
        num_pages (int): Number of pages to scrape
        output_filename (str): Output CSV filename
        browser (str): Browser to use ('firefox' or 'chrome')
        headless (bool): Whether to run browser in headless mode
    """
    # Use config values if parameters not provided
    num_pages = num_pages if num_pages is not None else config.NUM_PAGES
    output_filename = output_filename if output_filename is not None else config.OUTPUT_FILE
    browser = browser if browser is not None else config.BROWSER
    headless = headless if headless is not None else config.HEADLESS

    driver = setup_driver(browser, headless)
    base_url = "https://www.quicket.co.za/events/"

    try:
        with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Add Page Number to headers
            csv_writer.writerow(['Event Title', 'Event Location', 'Event Date', 'Event Time', 'Page Number'])

            # Load initial page
            driver.get(base_url)
            page_num = 1

            while page_num <= num_pages:
                print(f"Scraping page {page_num}")
                
                # Wait for events to load
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "l-event-item")))
                
                # Let the page fully render
                time.sleep(2)
                
                # Get the page source and parse with BeautifulSoup
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                events = soup.find_all('li', class_='l-event-item')
                print(f"Found {len(events)} events on page {page_num}")

                for event in events:
                    try:
                        # Extract event details using BeautifulSoup
                        title = event.find('div', class_='l-hit').text.strip()
                        location = event.find('div', class_='l-hit-venue').text.strip()
                        date_elements = event.find_all('div', class_='l-date')
                        
                        date = "N/A"
                        time_var = "N/A"
                        
                        if len(date_elements) >= 2:
                            date = date_elements[0].text.replace("Runs from", "").strip()
                            time_var = date_elements[1].text.strip()
                        
                        # Add page_num to the CSV row
                        csv_writer.writerow([title, location, date, time_var, page_num])
                        
                    except Exception as e:
                        print(f"Error extracting event details: {e}")
                        continue

                if page_num < num_pages:
                    try:
                        # Scroll to bottom before clicking next page
                        scroll_to_bottom(driver)
                        
                        # Find and click the next page button
                        next_button = wait.until(EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, "i.fa-solid.fa-angle-right.l-icon")))
                        driver.execute_script("arguments[0].scrollIntoView();", next_button)
                        time.sleep(1)  # Short pause after scrolling
                        next_button.click()
                        
                        # Wait for the new page to load
                        time.sleep(random.uniform(2, 4))
                    except (NoSuchElementException, TimeoutException) as e:
                        print(f"Navigation error: {e}")
                        print("No more pages available")
                        break

                page_num += 1
                # Random delay between pages
                time.sleep(random.uniform(1, 3))

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print(f"Scraping complete. Data saved to {output_filename}")

if __name__ == "__main__":
    scrape_quicket_events()