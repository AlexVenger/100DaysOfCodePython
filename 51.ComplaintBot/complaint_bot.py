from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

UPLOAD_SPEED = 2
DOWNLOAD_SPEED = 40


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
            options=Options()
        )
        self.down = 0
        self.up = 0
        with open("twitter_credentials.json") as twitter:
            data = json.load(twitter)
            self.email = data["email"]
            self.password = data["password"]
            self.username = data["username"]

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        button = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        button.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        self.down = float(download_speed)
        self.up = float(upload_speed)
        if self.down < DOWNLOAD_SPEED or self.up < UPLOAD_SPEED:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        # It doesn't send the tweet text because I didn't want to.
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        email_input_field = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        email_input_field.send_keys(self.email)
        next_button = self.driver.find_element(By.CSS_SELECTOR, ' div[style="color: rgb(255, 255, 255);"]')
        next_button.click()
        time.sleep(2)
        try:
            phone_or_username_input_field = self.driver.find_element(By.CSS_SELECTOR, 'input[autocapitalize="none"]')
            phone_or_username_input_field.send_keys(self.username)
            next_button = self.driver.find_element(By.CSS_SELECTOR, ' div[style="color: rgb(255, 255, 255);"]')
            next_button.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        password_input_field = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password_input_field.send_keys(self.password)
        next_button = self.driver.find_element(By.CSS_SELECTOR, ' div[style="color: rgb(255, 255, 255);"]')
        next_button.click()
        time.sleep(3)
        tweet_box = self.driver.find_element(
            By.CSS_SELECTOR,
            '.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr'
        )
        tweet_box.send_keys(f"Hey, KATV, why is my download speed {self.down} and my upload speed {self.up}"
                            f" if I'm paying for {DOWNLOAD_SPEED} and {UPLOAD_SPEED}?")
        time.sleep(10)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
