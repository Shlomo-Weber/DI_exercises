from flask import Flask
from flask import render_template
import productsdb

app = Flask(__name__)

@app.route('/')
def showshop():
    return render_template('shophome.html')

@app.route('/shop')
def products():
    products = productsdb.load_database()
    return render_template('products.html', products=products)



app.run(debug=True)