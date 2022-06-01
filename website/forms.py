from unicodedata import name
from wsgiref.validate import validator
from flask import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators

class Addproduct(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    keywords = TextAreaField('Keywords', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    
    image_1 = FileField('Image 1', validators = [FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif'])])
    image_2 = FileField('Image 2', validators = [FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif'])])
    image_3 = FileField('Image 3', validators = [FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif'])])