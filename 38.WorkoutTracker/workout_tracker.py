import requests
import json
import datetime

with open("nutrition.json") as key_file:
    keys = json.load(key_file)
    app_id = keys["app_id"]
    api_key = keys["api_key"]
    username = keys["username"]
    project_name = keys["project_name"]
    sheet_name = keys["sheet_name"]
    token = keys["token"]

nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}
nutrition_body = {
    "query": input("Tell me what exercises you did today: "),
    "gender": input("Your gender: "),
    "weight_kg": float(input("Your weight (kg): ")),
    "height_cm": float(input("Your height (cm): ")),
    "age": int(input("Your age: "))
}

response = requests.post(url=nutrition_url, json=nutrition_body, headers=nutrition_headers)
# print(response.text)

sheety_url = f"https://api.sheety.co/{username}/{project_name}/{sheet_name}"
sheety_headers = {
    "Authorization": f"Bearer {token}"
}
today = datetime.datetime.today()
for exercise in response.json()["exercises"]:
    sheety_body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=sheety_url, json=sheety_body, headers=sheety_headers)
    # print(response.text)
