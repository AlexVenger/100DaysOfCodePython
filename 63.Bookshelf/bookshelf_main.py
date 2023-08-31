from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from book_form import BookForm
from edit_form import EditForm
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = "shelf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
Bootstrap5(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Books(
            title=form.name.data,
            author=form.author.data,
            rating=form.rating.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect("/")
    return render_template("add.html", form=form)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    form = EditForm()
    book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    if form.validate_on_submit():
        new_rating = form.rating.data
        book.rating = new_rating
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", book=book, form=form)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

