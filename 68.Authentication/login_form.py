from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(
        validators=[DataRequired(), Length(min=8)],
        render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Sign In")
