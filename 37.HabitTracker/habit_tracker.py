import requests
import json
import datetime

with open("pixela_data.json") as pixela_data:
	pixela_json = json.load(pixela_data)
	token = pixela_json["token"]
	username = pixela_json["username"]

pixela_url = "https://pixe.la/v1/users"
token_header = {"X-USER-TOKEN": token}

# Dictionary of colors with translation just to make life a little easier
colors = {
	"green": "shibafu",
	"red": "momiji",
	"blue": "sora",
	"yellow": "ichou",
	"purple": "ajisai",
	"black": "kuro"
}


# shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple)
# and kuro (black) are supported as color kind.
def create_graph(graph_id: str, name: str, unit: str, data_type: str, color: str, timezone=None):
	graph_url = f"{pixela_url}/{username}/graphs"
	graph_config = {
		"id": graph_id,  # Validation rule: ^[a-z][a-z0-9-]{1,16}
		"name": name,
		"unit": unit,
		"type": data_type,  # int or float
		"color": color
	}
	if timezone is not None:
		graph_config["timezone"] = timezone
	response = requests.post(url=graph_url, json=graph_config, headers=token_header)
	print(response.text)


def add_pixel(graph_id: str, date: str, quantity: str):
	pixel_url = f"{pixela_url}/{username}/graphs/{graph_id}"
	pixel_config = {
		"date": date,
		"quantity": quantity
	}
	response = requests.post(url=pixel_url, json=pixel_config, headers=token_header)
	print(response.text)


def update_pixel(graph_id: str, date: str, quantity: str):
	pixel_url = f"{pixela_url}/{username}/graphs/{graph_id}/{date}"
	pixel_config = {
		"quantity": quantity
	}
	response = requests.put(url=pixel_url, json=pixel_config, headers=token_header)
	print(response.text)


def delete_pixel(graph_id: str, date: str):
	pixel_url = f"{pixela_url}/{username}/graphs/{graph_id}/{date}"
	response = requests.delete(url=pixel_url, headers=token_header)
	print(response.text)


# create_graph(
# 	graph_id="graph1",
# 	name="Reading Graph",
# 	unit="pages",
# 	data_type="int",
# 	color=colors["green"],
# 	timezone="Asia/Baku"
# )

add_pixel(
	graph_id="graph1",
	date=(datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d"),
	quantity="46"
)

# update_pixel(
# 	graph_id="graph1",
# 	date=datetime.date.today().strftime("%Y%m%d"),
# 	quantity="10"
# )

# delete_pixel(
# 	graph_id="graph1",
# 	date=datetime.date.today().strftime("%Y%m%d")
# )
