import wtforms
import flask_wtf
from wtforms import validators

class Products(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name', [validators.DataRequired(), validators.Length(max=30)])
    price = wtforms.IntegerField('Price', [validators.DataRequired()])
    category = wtforms.SelectField('Category', choices=[('laps', 'Laptops'), ('phone', 'Mobile Phones'), ('acc', 'Accessories')])
    stock = wtforms.IntegerField('Stock')
    image = wtforms.FileField('Image Upload')
    submit = wtforms.SubmitField('Submit')