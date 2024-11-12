from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (without opening a window)
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
driver.get("https://casesearch.courts.state.md.us/casesearch/")  # Replace with the URL you want to automate

# Wait for the page to load completely
time.sleep(15)  # Adjust the sleep time if needed to wait for the elements to load

# Find the checkbox element and click it
checkbox = driver.find_element(By.NAME, "disclaimer")
if not checkbox.is_selected():
    checkbox.click()

# Find the "I Agree" button and click it
agree_button = driver.find_element(By.XPATH, "//button[contains(text(), 'I Agree')]")
agree_button.click()

# Optionally, wait to see the result before closing the browser
time.sleep(10)

# Close the browser
driver.quit()
