import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Another way to run webdriver if you have chromedriver.exe

DRIVER_PATH = r"C:/Program Files/Google/chromedriver-win64/chromedriver.exe"

chrome_service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
