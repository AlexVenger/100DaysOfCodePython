from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

MY_NAME = "MDS (Me Doing Stuff)"
YEAR = datetime.now().year


@app.route("/")
def home():
	random_number = random.random()
	return render_template("index.html", num=random_number, name=MY_NAME, year=YEAR)


if __name__ == "__main__":
	app.run(debug=True)
