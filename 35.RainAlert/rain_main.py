import requests
import json

with open("api_key.json") as key_file:
    data = json.load(key_file)
    bot_token = data["bot_key"]
    user_id = data["user_id"]
    api_key = data["api_key"]


# I'm using a Telegram bot to send a message instead of Twilio SMS API because Twilio's policy is too intricate for me
def send_to_telegram(message):
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    try:
        telegram_response = requests.post(api_url, json={'chat_id': user_id, 'text': message})
    except Exception as e:
        print(e)


url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 40.409264,
    "lon": 49.867092,
    "appid": api_key
}
response = requests.get(url, params)
response.raise_for_status()
data = response.json()
country = data["city"]["country"]
city = data["city"]["name"]
data_list = data["list"]
for data in data_list:
    e_stop = False
    for weather_data in data["weather"]:
        if weather_data["id"] < 700:
            send_to_telegram(f"Umbrella situation in {city}, {country}")
            e_stop = True
            break
    if e_stop:
        break
