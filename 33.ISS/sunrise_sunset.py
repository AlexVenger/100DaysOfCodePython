import requests


def get_sunrise_and_sunset_time(latitude=40.409264, longitude=49.867092):
    response = requests.get(url="https://api.sunrise-sunset.org/json", params={
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    })
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    return {
        "sunrise": sunrise,
        "sunset": sunset
    }
