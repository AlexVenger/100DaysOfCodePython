# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import json

with open("credentials.json") as credentials:
    credential_data = json.load(credentials)
    tequila_key = credential_data["tequila_key"]
    sheety_token = credential_data["sheety_token"]
    sheety_username = credential_data["sheety_username"]
    sheety_project_name = credential_data["sheety_project_name"]
    sheety_prices = credential_data["sheety_prices"]
    sheety_users = credential_data["sheety_users"]
    bot_key = credential_data["bot_key"]
    user_id = credential_data["user_id"]

manager = DataManager(sheety_token, sheety_username, sheety_project_name, sheety_prices)
notifier = NotificationManager(bot_key, user_id)
data = FlightData(tequila_key, manager)
search = FlightSearch(tequila_key, manager, notifier)
data.set_iata_codes()
search.search_tickets()
