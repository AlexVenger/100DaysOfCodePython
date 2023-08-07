import requests
import json
from bs4 import BeautifulSoup
import smtplib
import lxml

with open("product_data.json") as product_data:
	data = json.load(product_data)
	url = data["url"]
	headers = data["headers"]
	email = data["email"]
	password = data["password"]
	to = data["to"]

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price_element = soup.select_one("span.a-offscreen")
price = float(price_element.text.replace("$", ""))

if price < 35:
	with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
		connection.starttls()
		connection.login(user=email, password=password)
		connection.sendmail(
			from_addr=email,
			to_addrs=to,
			msg=f"Subject: Amazon Price Drop Alert\n\nThe price of a product you wanted has dropped!\nCheck here: {url}"
		)
