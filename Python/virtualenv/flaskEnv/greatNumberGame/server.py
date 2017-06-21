from flask import Flask, session, redirect, render_template, request
import random
app = Flask(__name__)

app.secret_key = 'skds829298ejf9d@*(498#9821)'


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'state' not in session:
        session['state'] = 'newgame'
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'guess' in request.form:

        guess = int(request.form['guess'])
        print("Guess: " + str(guess) + ", Random #: " + str(session['num']))

        if guess > session['num']:
            session['state'] = 'high'
        elif guess < session['num']:
            session['state'] = 'low'
        else:
            session['state'] = 'win'
    print(session['state'])
    return render_template('index.html', state=session['state'], num=session['num'])


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
