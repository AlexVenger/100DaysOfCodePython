from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()], render_kw={"style": "width: 30ch"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)], render_kw={"style": "width: 30ch"})
    submit = SubmitField("Log In")
