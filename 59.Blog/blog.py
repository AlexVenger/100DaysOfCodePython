from flask import Flask, render_template, request, jsonify
import requests
import json
import smtplib


app = Flask(__name__)

blogs_url = "https://api.npoint.io/5deaf41b4f8078c817e6"
blogs = requests.get(blogs_url)
posts = blogs.json()
with open("email_credentials.json") as credentials:
    data = json.load(credentials)
    from_email = data["email"]
    password = data["password"]
    to = data["to"]


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<post_id>")
def post_page(post_id):
    for post in posts:
        if post["id"] == int(post_id):
            return render_template("post.html", post=post)
    return None


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to,
                msg=f"Subject: Contact with {name}\n\n{message}\nEmail: {email}\nPhone: {phone}"
            )

        return jsonify(message="success")


if __name__ == "__main__":
    app.run(debug=True)
