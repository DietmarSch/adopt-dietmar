from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Length, URL, number_range

class AddPetForm(FlaskForm):
    name = StringField('Name', validators = [InputRequired()])
    species = SelectField('Species', choices = [('cat', 'Cat'),('dog', 'Dog'), ("porcupine", "Porcupine")])
    photo_url = StringField('Photo_URL',validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[number_range(min=0, max=30)])
    notes= TextAreaField('Notes', validators=[Optional()])
    

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo_URL',validators=[Optional(), URL()])
    notes= TextAreaField('Notes', validators=[Optional()])
    available=BooleanField('Available ?')

