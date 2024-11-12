import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL for the form submission
url = "https://casesearch.courts.state.md.us/casesearch/inquirySearch.jis"

# Form data
form_data = {
    "lastName": "A%",                # Entering "A%" for a partial last name search
    "searchBasicAdvanced": "advanced", # Indicates advanced search
    "company2": "N",                  # Search for a person (not a business)
    "searchtype": "ouR+2O+eGQ7Hchl3aGbtkO4JVqDhVF7aWsqNpiEV6F8b6trb7AHswQ6Rf7jVYm4ufjHMXuCWHyvGf5BrhJAULRCasCBPHiQ/0RmEF2W6Wnk=", # Predefined hidden field value
    "submitButtonType": "submit",     # Indicates a search submission
    "accordion1Index": "1",
    "accordion2Index": "1"
}

# Function to generate a random X-Forwarded-For IP address
def generate_x_forwarded_for():
    """Generate a random X-Forwarded-For IP address."""
    ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip

# Setting up Chrome options for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Avoid using the sandbox (needed in some environments)

# Initialize WebDriver (assuming ChromeDriver is installed and in PATH)
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
driver.get(url)

# Wait for the page to load (you may need to adjust the time)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "lastName")))

# Fill out the form using Selenium's WebDriver
driver.find_element(By.NAME, "lastName").send_keys(form_data["lastName"])  # Enter lastName
driver.find_element(By.NAME, "searchBasicAdvanced").send_keys(form_data["searchBasicAdvanced"])  # Enter search type
driver.find_element(By.NAME, "company2").send_keys(form_data["company2"])  # Enter company type
driver.find_element(By.NAME, "searchtype").send_keys(form_data["searchtype"])  # Enter searchtype (hidden field)
driver.find_element(By.NAME, "submitButtonType").click()  # Submit the form

# Wait for the results to load
time.sleep(5)

# Save the result page HTML
with open("search_results.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# Print confirmation
print("Search completed and results saved to 'search_results.html'.")

# Close the WebDriver
driver.quit()
