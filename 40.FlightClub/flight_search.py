import requests
import datetime


class FlightSearch:
    # This class is responsible for structuring the flight data.
    def __init__(self, key, manager, notifier):
        self.key = key
        self.url = "https://api.tequila.kiwi.com/v2"
        self.headers = {
            "apikey": self.key,
            "accept": "application/json"
        }
        self.data_manager = manager
        self.notification_manager = notifier

    def search_tickets(self):
        url = self.url + "/search"
        rows = self.data_manager.get_rows().json()["prices"]
        today = datetime.date.today()
        cities = ""
        for row in rows:
            cities += f"{row['iataCode']},"
        cities = cities[:-1]
        params = {
            "fly_from": "BAK",
            "fly_to": cities,
            "date_from": (today + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (today + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "AZN",
            "one_for_city": 1
        }
        tickets = requests.get(url=url, params=params, headers=self.headers)
        data = tickets.json()["data"]
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        flight_prices = {}
        notifications = {}
        for datum in data:
            flight_prices[datum["cityCodeTo"]] = datum["price"]
            notifications[datum["cityCodeTo"]] = {
                "price": datum["price"],
                "dep_city": datum["cityFrom"],
                "dep_airport": datum["flyFrom"],
                "arr_city": datum["cityTo"],
                "arr_airport": datum["flyTo"],
                "from_date": datetime.datetime.strptime(datum["route"][0]["local_departure"], date_format).date(),
                "to_date": datetime.datetime.strptime(datum["route"][-1]["local_arrival"], date_format).date()
            }
        for row in rows:
            try:
                if row["lowestPrice"] > flight_prices[row["iataCode"]]:
                    notification = notifications[row["iataCode"]]
                    self.data_manager.edit_row(
                        row["city"], row["iataCode"], flight_prices[row["iataCode"]], row["id"])
                    self.notification_manager.cheapest_flight_alert(
                        price=notification["price"],
                        dep_city=notification["dep_city"],
                        dep_airport=notification["dep_airport"],
                        arr_city=notification["arr_city"],
                        arr_airport=notification["arr_airport"],
                        from_date=notification["from_date"],
                        to_date=notification["to_date"]
                    )
            except KeyError:
                continue
