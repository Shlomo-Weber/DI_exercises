from flask import Flask
from flask import render_template
from flask import request
import random, string
from Week_6.Day_3.exerform import Products
import db
app = Flask(__name__)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

app.config['SECRET_KEY'] = randomword(256)

@app.route('/')
def base():
    return render_template('exerbase.html')

@app.route('/addproducts/', methods=('GET', 'POST'))
def add_products():
    prod_form = Products()
    if request.method == 'GET':
        return render_template('add_products.html', form = prod_form)
    elif request.method == "POST" and prod_form.validate():
        name = prod_form.name.data
        price = prod_form.price.data
        category = prod_form.category.data
        stock = prod_form.stock.data
        dict = {'name':name, 'price':price, 'category': category, 'stock':stock}
        database = db.load_database()
        database.append(dict)
        db.update_database(database)
        return render_template('exerbase.html')

app.run()