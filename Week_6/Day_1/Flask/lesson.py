# Exercise 1
from flask import Flask
import datetime
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def say_hi():
    return "Hello there"

@app.route('/date')
def showdate():
    datenow = datetime.datetime.now()
    return f"It is {datenow}"

@app.route('/CV/<string:name>/<string:h1>/<string:h2>/<string:h3>')
def my_CV(name, h1, h2, h3):
    html = render_template('CV.html', name=name, h1=h1, h2=h2, h3=h3)
    return html


# Exercise 2

@app.route('/dateuntiljan')
def date_until_jan():
    jan = datetime.datetime(2021,1,1,1,1,1,1)
    diff = jan - datetime.datetime.now()
    return f"<h1>It's {diff} until January</h1>"

@app.route('/guess/<int:guess>')
def guessing_game(guess):
    num = random.randint(1,101)
    if guess == num:
        return "You won"
    elif guess == 42:
        return "you sly bastard"
    else:
        return "You suck"


if __name__ == "__main__":
    app.run(debug=True)