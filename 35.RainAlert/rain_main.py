import requests
import json

with open("api_key.json") as key_file:
    api_key = json.load(key_file)["api_key"]
url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 40.409264,
    "lon": 49.867092,
    "appid": api_key
}
response = requests.get(url, params)
response.raise_for_status()
data_list = response.json()["list"]
for data in data_list:
    e_stop = False
    for weather_data in data["weather"]:
        if weather_data["id"] < 700:
            print("Umbrella situation")
            e_stop = True
            break
    if e_stop:
        break
