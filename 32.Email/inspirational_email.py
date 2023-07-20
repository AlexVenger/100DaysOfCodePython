import smtplib
from datetime import datetime
import json
import random


def send_inspiration():
    # Create your own email_credentials.json with 3 keys:
    # email for your email address;
    # password for password;
    # to for the email address to which you'll send your email.
    # Add it to .gitignore to avoid data leaks
    with open("email_credentials.json") as credentials:
        data = json.load(credentials)
        email = data["email"]
        password = data["password"]
        to = data["to"]

    with open("quotes.txt") as quotes:
        quote = random.choice(quotes.readlines())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to,
            msg=f"Subject: Daily inspiration\n\n{quote}"
        )


weekday = datetime.now().weekday()
if weekday == 6:
    send_inspiration()
