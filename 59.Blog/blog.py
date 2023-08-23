from flask import Flask, render_template
import requests


app = Flask(__name__)

blogs_url = "https://api.npoint.io/5deaf41b4f8078c817e6"
blogs = requests.get(blogs_url)
posts = blogs.json()
print(posts)


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


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
