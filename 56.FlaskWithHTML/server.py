from flask import Flask, render_template

app = Flask(__name__)


@app.route("/goodbye")
def goodbye_world():
	return render_template("index1.html")


@app.route("/")
def start_page():
	return render_template("index2.html")


if __name__ == "__main__":
	app.run(debug=True)
