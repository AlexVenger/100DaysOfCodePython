from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


class EditForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired(), NumberRange(0, 10)])
    submit_button = SubmitField("Add Book")
