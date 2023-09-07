from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from util import cafe_to_dict, cafes_to_list

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random():
    cafe = Cafe.query.order_by(func.random()).first()
    cafe_dict = cafe_to_dict(cafe)
    return jsonify(cafe_dict)


@app.route("/all", methods=["GET"])
def get_all():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
    cafe_list = cafes_to_list(cafes)
    return jsonify(cafe_list)


@app.route("/search", methods=["GET"])
def search():
    if "loc" in request.args.keys():
        location = request.args.get("loc")
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location).order_by(Cafe.id)).scalars()
        cafe_list = cafes_to_list(cafes)
        return jsonify(cafe_list)
    else:
        return jsonify({
            "error": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        })


@app.route("/add", methods=["POST"])
def add():
    data = request.json
    try:
        cafe = Cafe(
            name=data["name"],
            map_url=data["map_url"],
            img_url=data["img_url"],
            location=data["location"],
            seats=data["seats"],
            has_toilet=data["has_toilet"],
            has_wifi=data["has_wifi"],
            has_sockets=data["has_sockets"],
            can_take_calls=data["can_take_calls"],
            coffee_price=data["coffee_price"] if "coffee_price" in data.keys() else None
        )
        db.session.add(cafe)
        db.session.commit()
        return jsonify({
            "response": {
                "success": "The cafe has been added successfully!"
            }
        })
    except KeyError:
        return jsonify({
            "response": {
                "failure": "Required data is missing!"
            }
        })


if __name__ == '__main__':
    app.run(debug=True)
