from flask import Flask,flash
from flask import render_template
from flask import request
import random, string
from Week_6.Day_3.exerform import Products
import db
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

app.config['SECRET_KEY'] = randomword(256)

@app.route('/')
def base():
    return render_template('exerbase.html')

@app.route('/addproducts', methods=('GET', 'POST'))
def add_products():
    prod_form = Products()
    if request.method == 'GET':
        return render_template('add_products.html', form = prod_form)
    elif request.method == "POST" and prod_form.validate():
        items = db.load_database()
        prod_id = len(items)
        name = prod_form.name.data
        price = prod_form.price.data
        category = prod_form.category.data
        stock = prod_form.stock.data

        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save('static/images/' + filename)

        dict = {'id':prod_id, 'name':name, 'price':price, 'category': category, 'stock':stock, 'image':filename}
        database = db.load_database()
        database.append(dict)
        db.update_database(database)
        flash("Your info has been successfully saved")
        return render_template('add_products.html', form =prod_form)

@app.route('/products')
def products():
    products = db.load_database()

    return render_template('exerproducts.html', products = products)

@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    products = db.load_database()
    return render_template('exerprod_details.html', product=products[product_id])

app.run(debug=True)