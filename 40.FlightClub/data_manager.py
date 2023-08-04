import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, token, username, project_name, sheet_name):
        self.token = token
        self.username = username
        self.project_name = project_name
        self.sheet_name = sheet_name
        self.url = f"https://api.sheety.co/{self.username}/{self.project_name}/{self.sheet_name}"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_rows(self):
        return requests.get(url=self.url, headers=self.headers)

    def add_row(self, city, code, price):
        body = {
            "price": {
                "city": city,
                "iataCode": code,
                "price": price
            }
        }
        return requests.post(url=self.url, headers=self.headers, json=body)

    def edit_row(self, city, code, price, row_id):
        url = self.url + f"/{row_id}"
        body = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price
            }
        }
        return requests.put(url=url, json=body, headers=self.headers)

    def delete_row(self, row_id):
        url = self.url + f"/{row_id}"
        return requests.delete(url=url, headers=self.headers)
