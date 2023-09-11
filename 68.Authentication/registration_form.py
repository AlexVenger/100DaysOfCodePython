from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
	name = StringField(validators=[DataRequired()], render_kw={"placeholder": "Name"})
	email = EmailField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	password = PasswordField(
		validators=[DataRequired(), Length(min=8), EqualTo(fieldname="confirm_password", message="Passwords mismatch!")],
		render_kw={"placeholder": "Password"}
	)
	confirm_password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
	submit = SubmitField("Sign Up")
