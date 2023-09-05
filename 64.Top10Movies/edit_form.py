from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange


class EditForm(FlaskForm):
    rating = FloatField(f"Your Rating out of 10:", validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField("Your Review:")
    submit_button = SubmitField("Done")
