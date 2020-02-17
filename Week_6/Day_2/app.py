from flask import Flask
import datetime
from flask import render_template

import db
app = Flask(__name__)

@app.route('/')
def home():# CONTROLLER

    # MODEL
    products = db.load_database()

    # VIEW
    return render_template("home.html", products=products)

app.run()