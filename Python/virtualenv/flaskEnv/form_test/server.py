from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# you need to set a secret key for security purposes
app.secret_key = 'skds829298ejf9d@*(498#9821)'
# routing rules and rest of server.py below


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
    return redirect('/show')


@app.route('/show')
def show_user():
    return render_template('user.html')


app.run(debug=True)
