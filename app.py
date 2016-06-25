from flask import Flask, request, render_template
from banners import Categories

app = Flask(__name__)


conffile = 'config.csv'
conf = Categories(conffile)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/banner")
def banner():
    cats = request.args.get("categories").split(',')
    # image = "http://c7.staticflickr.com/8/7424/9262102694_a79aa1b44d.jpg"
    image = conf.get_categories(cats)
    return render_template("banner.html", image=image)