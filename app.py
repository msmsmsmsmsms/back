from flask import Flask, render_template, url_for, request
from main import main, get_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def get_search():
    q = request.form['search']
    link = get_data(q)
    return link


if __name__ == "__main__":
    app.run(debug=True)