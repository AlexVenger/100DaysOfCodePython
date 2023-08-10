from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

with open("linkedin_credentials.json") as credentials:
	data = json.load(credentials)
	email = data["email"]
	password = data["password"]

driver = webdriver.Chrome(
	service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
	options=Options()
)

driver.get("https://linkedin.com")
time.sleep(3)
email_input = driver.find_element(By.ID, "session_key")
email_input.send_keys(email)
password_input = driver.find_element(By.ID, "session_password")
password_input.send_keys(password)
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.click()
time.sleep(1)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3676698104&distance=25&f_AL=true&f_WT=2&geoId=92000000&keywords=python%20developer&refresh=true")
time.sleep(2)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
apply_button.click()
time.sleep(5)
# jobs = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container > li")
# actions = ActionChains(driver)
# for job in jobs:
# 	actions.move_to_element(job)
# 	job.click()
# 	time.sleep(2)
# 	save_button = driver.find_element(
# 		By.CSS_SELECTOR,
# 		".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary"
# 	)
# 	save_button.click()
# 	time.sleep(2)

driver.quit()
