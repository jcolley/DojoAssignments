from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return ("No ninjas here")


@app.route('/ninja')
def ninja():
    return ('<img src="/static/img/tmnt.png" alt="TMNT">')


@app.route('/ninja/<color>')
def ninjas(color):
    return render_template(
        "ninja.html",
        img1="/static/img/leonardo.jpg",
        img2="/static/img/michelangelo.jpg",
        img3="/static/img/raphael.jpg",
        img4="/static/img/donatello.jpg",
        img5="/static/img/notapril.jpg",
        color=color
    )


app.run(debug=True)
