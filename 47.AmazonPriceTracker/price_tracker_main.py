import requests
import json
from bs4 import BeautifulSoup

with open("product_data.json") as product_data:
	data = json.load(product_data)
	url = data["url"]
	headers = data["headers"]

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

price = soup.select_one("#corePrice_feature_div span.a-offscreen")
print(price.text)
