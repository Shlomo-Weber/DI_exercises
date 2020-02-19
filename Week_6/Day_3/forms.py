import flask_wtf
import wtforms
from wtforms import validators

class FormLogin(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name')
    password = wtforms.PasswordField('Password')
    info = wtforms.StringField('Info')
    submit = wtforms.SubmitField('Submit')