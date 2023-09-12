import flask
import sqlalchemy.exc
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap5
from registration_form import RegistrationForm
from login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(
                email=form.email.data,
                password=generate_password_hash(
                    password=form.password.data,
                    method="pbkdf2:sha256",
                    salt_length=8
                ),
                name=form.name.data
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("secrets", name=user.name))
        except sqlalchemy.exc.IntegrityError:
            flash("User with such email already exists!")
            return redirect(url_for("register"))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if not user:
            flask.flash("Such user doesn't exist!")
            return redirect(url_for("login"))
        if check_password_hash(user.password, form.password.data):
            login_user(user)
            if user.is_authenticated:
                return redirect(url_for("secrets", name=user.name))
        else:
            flask.flash("Wrong password!")
    return render_template("login.html", form=form)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=request.args.get("name"))


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/download', methods=['GET'])
@login_required
def download():
    return send_from_directory(app.static_folder, 'files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
