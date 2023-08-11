from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import json


def login_and_go_to_main_page(email, password):
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
	time.sleep(10)
	driver.get(
		"https://www.linkedin.com/jobs/search/?currentJobId=3676698104&distance=25&f_AL=true&f_WT=2&geoId=92000000&keywords=python%20developer&refresh=true")
	time.sleep(3)
	return driver


def apply_to_job(driver, job):
	job.click()
	time.sleep(2)
	try:
		apply_button = driver.find_element(
			By.CSS_SELECTOR,
			".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view"
		)
		apply_button.click()
	except NoSuchElementException:
		return
	next_button = WebDriverWait(driver, 10).until(
		lambda x: x.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]'))
	next_button.click()
	try:
		review_button = WebDriverWait(driver, 10).until(
			lambda x: x.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
		)
		review_button.click()
		time.sleep(1)
		submit_button = WebDriverWait(driver, 10).until(
			lambda x: x.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
		)
		submit_button.click()
		time.sleep(1)
		close_button = WebDriverWait(driver, 10).until(
			lambda x: x.find_elements(By.CLASS_NAME, "mercado-match")[0]
		)
		close_button.click()
	except (NoSuchElementException, TimeoutException):
		cancel_button = driver.find_element(By.CSS_SELECTOR, 'li-icon[type="cancel-icon"]')
		cancel_button.click()
		time.sleep(1)
		discard_button = driver.find_element(By.CSS_SELECTOR, 'button[class="artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"]')
		discard_button.click()
		time.sleep(2)
		# save_button = driver.find_element(
		# 	By.CSS_SELECTOR,
		# 	".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary"
		# )
		# save_button.click()
		# try:
		# 	close_notification_button = driver.find_element(
		# 		By.CSS_SELECTOR,
		# 		'button[class="artdeco-toast-item__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]'
		# 	)
		# 	close_notification_button.click()
		# except NoSuchElementException:
		# 	try:
		# 		close_notification_button = driver.find_elements(
		# 			By.CLASS_NAME,
		# 			'mercado-match'
		# 		)[1]
		# 		close_notification_button.click()
		# 	except NoSuchElementException:
		# 		return


with open("linkedin_credentials.json") as credentials:
	data = json.load(credentials)
	email = data["email"]
	password = data["password"]

driver = login_and_go_to_main_page(email, password)
jobs = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container > li")

for job in jobs:
	apply_to_job(driver, job)
	time.sleep(5)

driver.quit()
