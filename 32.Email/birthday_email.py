# Extra Hard Starting Project #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas
from datetime import datetime
import random
import json


def send_birthday_wish(celebrators_email, celebrators_name):
    # Create your own email_credentials.json with 3 keys:
    # email for your email address;
    # password for password;
    # to for the email address to which you'll send your email.
    # Add it to .gitignore to avoid data leaks
    with open("email_credentials.json") as credentials:
        data = json.load(credentials)
        email = data["email"]
        password = data["password"]

    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_template:
        message = letter_template.read().replace("[NAME]", celebrators_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=celebrators_email,
            msg=f"Subject: Happy Birthday!\n\n{message}"
        )


birthdays = pandas.read_csv("birthdays.csv")
for birthday in birthdays.to_dict(orient="records"):
    today = datetime.now()
    if int(birthday["day"]) == today.day and int(birthday["month"]) == today.month:
        send_birthday_wish(birthday["email"], birthday["name"])
