from flask import Flask, render_template, url_for, request
from main import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def get_search():
    q = request.form['search']
    context_mvideo, context_citylink, context_eldorado = main(q)
    return render_template("card.html", context_mvideo=context_mvideo, context_citylink=context_citylink, context_eldorado=context_eldorado, q=q)


if __name__ == "__main__":
    app.run(debug=True)