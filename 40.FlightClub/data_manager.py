import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, token, username, project_name, price_sheet, user_sheet):
        self.token = token
        self.username = username
        self.project_name = project_name
        self.price_sheet = price_sheet
        self.user_sheet = user_sheet
        self.prices_url = f"https://api.sheety.co/{self.username}/{self.project_name}/{self.price_sheet}"
        self.users_url = f"https://api.sheety.co/{self.username}/{self.project_name}/{self.user_sheet}"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_rows(self):
        return requests.get(url=self.prices_url, headers=self.headers)

    def add_row(self, city, code, price):
        body = {
            "price": {
                "city": city,
                "iataCode": code,
                "price": price
            }
        }
        return requests.post(url=self.prices_url, headers=self.headers, json=body)

    def edit_row(self, city, code, price, row_id):
        url = self.prices_url + f"/{row_id}"
        body = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price
            }
        }
        return requests.put(url=url, json=body, headers=self.headers)

    def delete_row(self, row_id):
        url = self.prices_url + f"/{row_id}"
        return requests.delete(url=url, headers=self.headers)

    def get_users(self):
        return requests.get(self.users_url, headers=self.headers)

    def get_emails(self):
        users = self.get_users().json()
        emails = []
        for user in users["users"]:
            emails.append(user["email"])
        return emails

