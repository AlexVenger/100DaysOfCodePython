import requests


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, bot_key, user_id):
        self.bot_key = bot_key
        self.user_id = user_id

    def cheapest_flight_alert(self, price, dep_city, dep_airport, arr_city, arr_airport, from_date, to_date):
        message = f"New cheapest flight found!\nFor {price} AZN from {dep_city}-{dep_airport} to " \
                  f"{arr_city}-{arr_airport} from {from_date} to {to_date}"
        api_url = f'https://api.telegram.org/bot{self.bot_key}/sendMessage'
        try:
            requests.post(api_url, json={'chat_id': self.user_id, 'text': message})
        except Exception as e:
            print(e)
