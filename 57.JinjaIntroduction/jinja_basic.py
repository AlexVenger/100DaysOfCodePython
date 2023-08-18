from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

MY_NAME = "MDS (Me Doing Stuff)"
YEAR = datetime.now().year


@app.route("/")
def home():
	random_number = random.random()
	return render_template("homepage.html", num=random_number, name=MY_NAME, year=YEAR)


@app.route("/guess/<name>")
def guesser(name: str):
	params = {"name": name}
	age_data = requests.get(url="https://api.agify.io/", params=params)
	age = age_data.json()["age"]
	gender_data = requests.get(url="https://api.genderize.io/", params=params)
	gender = gender_data.json()["gender"]
	return render_template("guess.html", name=name.capitalize(), age=age, gender=gender)


if __name__ == "__main__":
	app.run(debug=True)
