from flask import Flask, request, redirect, render_template, session, flash, Markup
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "krhre*#*(#ui3492@pOEIfj!"
mysql = MySQLConnector(app, 'registration')
fbcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    if session.get('id'):
        message = Markup('Logged in as: ' +
                         session['email'] +
                         '<br><button type="submit" name="submit" value="logout">Log Out</button>')
        flash(message)
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create():
    if session.get('id'):
        message = Markup('Logged in as: ' +
                         session['email'] +
                         '<br><button type="submit" name="submit" value="logout">Log Out</button>')
        flash(message)
    # Set some session data
    session['names'] = request.form['name']
    session['email'] = request.form['email']

    # Do some nifty single-field name splitting for DB storage
    names = request.form['name'].split()
    try:
        first_name = names[0]
    except:
        first_name = ''
    try:
        last_name = names[1]
    except:
        last_name = ''

    if request.form['submit'] == "register":
        # Form Validation
        if len(first_name) < 2:
            flash("First name must be more than 2 characters")
        elif len(last_name) < 2:
            flash("Last name must be more than 2 characters")
        elif len(request.form['email']) < 1:
            flash("Email cannot be blank!")
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
        elif len(request.form['password']) < 8:
            flash("You must enter a password of at least 8 characters")
        else:
            query = "INSERT INTO users (username, email, password, created_at) VALUES (:username, :email, :passhash, NOW())"
            data = {
                'username': request.form['name'],
                'email': request.form['email'],
                'passhash': fbcrypt.generate_password_hash(request.form['password'])
            }

            session['id'] = mysql.query_db(query, data)
            return redirect('/success')

    elif request.form['submit'] == "login":
        if session.get('id'):
            session.clear()
            flash("You have been logged out.")
            return redirect('/')
        if len(request.form['email']) < 1:
            flash("Email cannot be blank!")
            return redirect('/')

        query = "SELECT id, password FROM users WHERE email = :email LIMIT 1"
        data = {
            'email': request.form['email']
        }
        userpass = request.form['password']
        udata = mysql.query_db(query, data)

        if fbcrypt.check_password_hash(udata[0]['password'], userpass):
            session['id'] = udata[0]['id']
            return redirect('/success')
        else:
            flash("Incorrect Username or Password")
            return redirect('/')

    elif request.form['submit'] == "logout":
        session.clear()

    return redirect('/')


@app.route('/success')
def success():
    if session.get('id'):
        message = Markup('Logged in as: ' +
                         session['email'] +
                         '<br><button type="submit" name="submit" value="logout">Log Out</button>')
        flash(message)
        return render_template('success.html')

    return redirect('/')


app.run(debug=True)
