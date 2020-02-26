from flask_wtf import *
from wtforms import *
from wtforms import validators
from wtforms.validators import data_required
class AddBook(FlaskForm):
    title = StringField(label='Title', validators= [data_required()])
    author = StringField(label='Author')
    pub_date = DateField(label='Publication Date')
    price = FloatField(label='Price', default=0)
    submit = SubmitField()