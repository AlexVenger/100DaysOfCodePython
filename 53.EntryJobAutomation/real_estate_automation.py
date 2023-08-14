from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import requests

url = 'https://www.zillow.com/search/GetSearchPageState.htm'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

houses = []
for page in range(1, 3):
    params = {
        "searchQueryState": json.dumps({
            "pagination": {},
            "mapBounds": {
                "west": -122.80274162564864,
                "east": -122.07489738736739,
                "south": 37.59684986023336,
                "north": 37.88463461631411
            },
            "isMapVisible": True,
            "filterState": {
                "price": {
                    "max": 872627
                },
                "beds": {
                    "min": 1
                },
                "isForSaleForeclosure": {
                    "value": False
                },
                "monthlyPayment": {
                    "max": 3000
                },
                "isAuction": {
                    "value": False
                },
                "isNewConstruction": {
                    "value": False
                },
                "isForRent": {
                    "value": True
                },
                "isForSaleByOwner": {
                    "value": False
                },
                "isComingSoon": {
                    "value": False
                },
                "isForSaleByAgent": {
                    "value": False
                }
            },
            "isListVisible": True
        }),
        "wants": json.dumps(
            {
                "cat1": ["listResults", "mapResults"],
                "cat2": ["total"]
            }
        ),
        "requestId": 3
    }

    # send request
    page = requests.get(url, headers=headers, params=params)

    # get json data
    json_data = page.json()
    # with open("chungus.json", "w") as chungus:
    #     json.dump(json_data, chungus, indent=2)

    # loop via data
    for house in json_data['cat1']['searchResults']['listResults']:
        # print(house)
        houses.append(house)


# show data
print('Total houses - {}'.format(len(houses)))

links = []
prices = []
addresses = []

# show info in houses
for house in houses:
    if house["detailUrl"][0:4] != "http":
        links.append(f"https://www.zillow.com{house['detailUrl']}")
    else:
        links.append(house["detailUrl"])
    if "units" in house.keys():
        prices.append(house["units"][0]["price"])
    else:
        prices.append(house["price"])
    addresses.append(house["address"])

print(links)
print(prices)
print(addresses)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="115.0.5790.170").install()),
    options=Options()
)

with open("data.json") as data:
    data = json.load(data)
    form_url = data["form_url"]
for i in range(len(houses)):
    driver.get(form_url)
    time.sleep(1)
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_input = inputs[0]
    price_input = inputs[1]
    link_input = inputs[2]

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    submit_button.click()
    time.sleep(3)
