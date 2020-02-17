from flask import Flask
import datetime
from flask import render_template
import  productsdb

app = Flask(__name__)

@app.route('/')
def say_whatsup():
    return "What's good"

@app.route('/date')
def daytime_greeting():
    time = datetime.datetime.now()
    hour = time.hour
    morn = hour >=8 and hour <=12
    aft = hour >=12 and hour <17
    eve = hour >=17 and hour <=21
    if morn:
        return "Good morning"
    elif aft:
        return "Good afternoon"
    elif eve:
        return "Good evening"
    else:
        return "Good night"




app.run()