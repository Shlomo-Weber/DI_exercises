from flask import Flask
import datetime
from flask import render_template
from flask import request

import db
app = Flask(__name__)

@app.route('/')
def home():# CONTROLLER

    # MODEL
    products = db.load_database()

    # VIEW
    return render_template("home.html", products=products)
@app.route('/login', method=('GET', 'POST'))
def login():
    if request.method == 'GET':
        pass
    if request.method =="POST":
        pass

app.run()