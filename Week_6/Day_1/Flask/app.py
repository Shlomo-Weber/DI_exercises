from flask import Flask
import pizza
from flask import request
from flask import render_template


# new app in the flask variable
app = Flask(__name__)

# Routes
@app.route('/') #To run something not specific
def hello_world():
    return 'Hello, World!'

@app.route('/home', defaults = {'name': "Stranger"})
@app.route('/home/<string:name>')
def home(name):
    return f"<h1 style='color:red;'>Welcome {name}!</h1> "


@app.route('/pizza/<int:size>/<string:top1>/<string:top2>')
def pizza1(size, top1, top2):
    return pizza.make_pizza(size, top1, top2)

@app.route('/custompizza/<path:args>')
def custom_pizza(args):
    args = args.split('/')
    return pizza.make_pizza(args[0], *args[1:])

@app.route('/getpizza', methods = ['GET'])
# link is getpizza?size =''& top1 = ''& top2 ='' & top3 = ''
def get_pizza():
    size = request.args.get("size")
    top1 = request.args.get("top1")
    top2 = request.args.get("top2")
    top3 = request.args.get("top3")
    return pizza.make_pizza(size, top1, top2, top3)


# Start the App
if __name__ == "__main__":
    app.run(debug=True)