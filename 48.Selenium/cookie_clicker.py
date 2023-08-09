from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

driver = webdriver.Chrome(
	service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
	options=Options()
)

driver.get("https://orteil.dashnet.org/cookieclicker/")
# Wait for the page to load
time.sleep(5)

language_select = driver.find_element(By.ID, "langSelect-EN")
language_select.click()
time.sleep(2)

cookie = driver.find_element(By.ID, "bigCookie")

now = datetime.datetime.now()
end_time = now + datetime.timedelta(minutes=5)
checkpoint = now
five_seconds = datetime.timedelta(seconds=5)

while now <= end_time:
	cookie.click()
	if now - checkpoint >= five_seconds:
		checkpoint = datetime.datetime.now()
		upgrades = driver.find_elements(By.CSS_SELECTOR, "div#upgrades div.crate.upgrade.enabled")
		if len(upgrades) > 0:
			upgrades[-1].click()
		cookie.click()
		store_items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
		if len(store_items) > 0:
			store_items[-1].click()
	now = datetime.datetime.now()

cookie_count = driver.find_element(By.ID, "cookies")
print(cookie_count.text)

# Pause to witness the final result
time.sleep(5)

driver.quit()
