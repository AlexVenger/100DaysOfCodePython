from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from edit_form import create_edit_form
from add_movie_form import AddMovieForm

MOVIES_URL = "https://api.themoviedb.org/3/search/movie"
GET_MOVIE_URL = "https://api.themoviedb.org/3/movie/"
with open("api_token.json") as token_file:
    data = json.load(token_file)
    token = data["token"]

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
db.init_app(app)
Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    form = create_edit_form(movie.ranking)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        if form.review.data is not None and form.review.data != "":
            movie.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        params = {"query": form.title.data}
        headers = {"Authorization": f"Bearer {token}"}
        movies_response = requests.get(MOVIES_URL, params=params, headers=headers)
        movies = movies_response.json()["results"]
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/select/<movie_id>")
def select(movie_id):
    url = GET_MOVIE_URL + str(movie_id)
    headers = {"Authorization": f"Bearer {token}"}
    movie_info = requests.get(url, headers=headers).json()
    movie = Movie(
        title=movie_info["original_title"],
        description=movie_info["overview"],
        year=int(movie_info["release_date"][0:4]),
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_info['poster_path']}",
        rating=0,
        review="",
        ranking=10
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(f"/edit/{movie.id}")


if __name__ == '__main__':
    app.run(debug=True)
