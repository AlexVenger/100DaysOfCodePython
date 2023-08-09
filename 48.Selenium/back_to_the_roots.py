from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

driver = webdriver.Chrome(
	service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
	options=Options()
)

driver.get("https://www.python.org/")

xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li'

elements = {}

for i in range(5):
	time = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/time')
	a = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/a')

	elements[i] = {
		"date": datetime.fromisoformat(time.get_attribute("datetime")).date(),
		"name": a.text
	}

print(elements)

driver.close()
