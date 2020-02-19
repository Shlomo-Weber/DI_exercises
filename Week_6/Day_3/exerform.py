import wtforms
import flask_wtf
from wtforms import validators

class Products(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name', [validators.DataRequired(), validators.Length(max=30)])
    price = wtforms.IntegerField('Price', [validators.DataRequired()])
    category = wtforms.StringField('Category',[validators.DataRequired()])
    stock = wtforms.IntegerField('Stock')
    submit = wtforms.SubmitField('Submit')
