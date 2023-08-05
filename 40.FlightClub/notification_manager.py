import requests
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, bot_key, user_id, email, password):
        self.bot_key = bot_key
        self.user_id = user_id
        self.email = email
        self.password = password

    def send_notification(self, notifications=dict, emails=None):
        message = f"New cheapest flight found!"
        for notification in notifications:
            message += f"\nFor {notification['price']} AZN from " \
                       f"{notification['dep_city']}-{notification['dep_airport']} to " \
                       f"{notification['arr_city']}-{notification['arr_airport']} from " \
                       f"{notification['from_date']} to {notification['to_date']}"
        if emails is None:
            self.telegram_alert(message)
        else:
            self.email_alert(emails, message)

    def telegram_alert(self, message: str):
        api_url = f'https://api.telegram.org/bot{self.bot_key}/sendMessage'
        try:
            requests.post(api_url, json={'chat_id': self.user_id, 'text': message})
        except Exception as e:
            print(e)

    def email_alert(self, emails: list[str], message: str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for receiver in emails:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=receiver,
                    msg=f"Subject: Cheap Tickets Alert\n\n{message}"
                )
