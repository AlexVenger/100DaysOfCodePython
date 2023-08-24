from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
	if request.method == "POST":
		return f"Username: {request.form['username']}"
	return "Yeetus"


if __name__ == "__main__":
	app.run(debug=True)
