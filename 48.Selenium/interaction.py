import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
	service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
	options=Options()
)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# special_statistics = driver.find_element(by=By.CSS_SELECTOR, value='a[title="Special:Statistics"]')
# print(special_statistics.text)
#
# driver.quit()

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("Big")
last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Chungus")
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("big_chungus@yeet.com")
submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()

time.sleep(5)

driver.quit()
