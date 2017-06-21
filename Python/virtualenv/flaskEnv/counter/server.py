from flask import Flask, render_template, session, redirect
app = Flask(__name__)
# you need to set a secret key for security purposes
app.secret_key = 'skds829298ejf9d@*(498#9821)'
# routing rules and rest of server.py below


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template("index.html")


@app.route('/plus2')
def plus2():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = -1
    return redirect('/')

app.run(debug=True)
