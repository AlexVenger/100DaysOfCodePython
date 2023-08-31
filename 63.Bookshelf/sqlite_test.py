import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     """CREATE TABLE books (
#     id INTEGER PRIMARY KEY,
#     title VARCHAR(250) NOT NULL UNIQUE,
#     author VARCHAR(250) NOT NULL,
#     rating FLOAT NOT NULL
#     )
#     """
# )

# cursor.execute(
#     """INSERT INTO books VALUES(1, 'Dubliners', 'James Joyce', 8)"""
# )
# db.commit()

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    book = Books(id=1, title="Dubliners", author="James Joyce", rating=9)
    db.session.add(book)
    db.session.commit()

if __name__ == "main":
    app.run(debug=True)
