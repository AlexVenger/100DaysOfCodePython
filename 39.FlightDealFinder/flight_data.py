import requests


class FlightData:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, key, manager):
        self.key = key
        self.url = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": self.key,
            "accept": "application/json"
        }
        self.data_manager = manager

    def set_iata_codes(self):
        url = self.url + "/locations/query"
        rows_response = self.data_manager.get_rows()
        rows = rows_response.json()["prices"]
        for row in rows:
            if row["iataCode"] == "":
                params = {
                    "term": row["city"],
                    "location_types": "city"
                }
                response = requests.get(url=url, params=params, headers=self.headers)
                data = response.json()
                code = data["locations"][0]["code"]
                self.data_manager.edit_row(row["city"], code, row["lowestPrice"], row["id"])
