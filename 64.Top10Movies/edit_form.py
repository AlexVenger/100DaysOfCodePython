from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange


def create_edit_form(ranking):
    class EditForm(FlaskForm):
        rating = FloatField(f"Your Rating out of {ranking}:", validators=[DataRequired(), NumberRange(0, ranking)])
        review = StringField("Your Review:")
        submit_button = SubmitField("Done")

    return EditForm()
