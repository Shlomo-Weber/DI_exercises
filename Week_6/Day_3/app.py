from flask import Flask
import datetime
from flask import render_template
from flask import request
from forms import *
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'herp derp'
@app.route('/')
def home():# CONTROLLER

    # MODEL
    products = db.load_database()

    # VIEW
    return render_template("home.html", products=products)

@app.route('/login', methods=('GET', 'POST'))
def login():
    login_form = FormLogin()
    if request.method == 'GET':
        return render_template('login.html', form=login_form)



app.run()