import requests
from datetime import datetime
from sunrise_sunset import get_sunrise_and_sunset_time
import json
import smtplib
import time

MY_LATITUDE = 40.409264
MY_LONGITUDE = 49.867092


def send_email():
    with open("../32.Email/email_credentials.json") as credentials:
        data = json.load(credentials)
        email = data["email"]
        password = data["password"]
        to = data["to"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to,
            msg=f"Subject: Look Up\n\nThe ISS is somewhere above you"
        )


def check_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_json = response.json()["iss_position"]
    iss_longitude = float(data_json["longitude"])
    iss_latitude = float(data_json["latitude"])

    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        day_info = get_sunrise_and_sunset_time()
        current_hour = datetime.now().hour
        if current_hour < day_info["sunrise"] or current_hour > day_info["sunset"]:
            send_email()


while True:
    check_iss_position()
    time.sleep(60)
