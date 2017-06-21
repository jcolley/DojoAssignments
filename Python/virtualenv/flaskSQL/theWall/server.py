from flask import Flask, request, redirect, render_template, session, flash, Markup
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "krhre*#*(#ui3492@pOEIfj!"
mysql = MySQLConnector(app, 'thewall')
fbcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    if session.get('logout'):
        session.clear()
        flash("Incorrect Username or Password")
    if session.get('user'):
        return redirect('/wall')

    return render_template('index.html')


@app.route('/register', methods=['POST'])
def create():
    # send a logged-in user to the Wall
    if session.get('user'):
        return redirect('/wall')

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
            query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :passhash, NOW())"
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': request.form['email'],
                'passhash': fbcrypt.generate_password_hash(request.form['password'])
            }

            session['id'] = mysql.query_db(query, data)
            session['userpass'] = request.form['password']

            return redirect('/login')

    elif request.form['submit'] == "login":
        if not session.get('userpass'):
            session['userpass'] = request.form['password']
        if not session.get('email'):
            session['email'] = request.form['email']

        return redirect('/login')

    elif request.form['submit'] == "logout":
        session.clear()

    return redirect('/')


@app.route('/wall')
def wall():
    if not session.get('user'):
        return redirect('/')

    query = "SELECT messages.id, messages.message, CONCAT(first_name, ' ', last_name) AS author, DATE_FORMAT(messages.created_at,'%b %d %Y') AS date FROM messages LEFT JOIN users ON messages.user_id=users.id ORDER BY messages.created_at DESC"
    session['messages'] = mysql.query_db(query)
    query = "SELECT comments.id, comments.comment, comments.message_id, CONCAT(first_name, ' ', last_name) AS author, DATE_FORMAT(comments.created_at,'%b %d %Y') AS date FROM comments LEFT JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC"
    session['comments'] = mysql.query_db(query)

    return render_template('wall.html', all_messages=session['messages'], msg_comments=session['comments'])


@app.route('/post', methods=['POST'])
def post():
    print request.form['submit']
    if request.form['submit'] == 'message':
        try:
            query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
            data = {
                'user_id': session['user']['id'],
                'message': request.form['message']
            }
            mysql.query_db(query, data)
        except:
            pass
    elif request.form['submit'] == 'comment':
        try:
            query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
            data = {
                'user_id': session['user']['id'],
                'message_id': request.form['message_id'],
                'comment': request.form['comment']
            }
            mysql.query_db(query, data)
        except:
            pass
    return redirect('/wall')


@app.route('/login')
def login():
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
        'email': session['email']
    }
    try:
        session['user'] = mysql.query_db(query, data)
        session['user'] = session['user'][0]
        if fbcrypt.check_password_hash(session['user']['password'], session['userpass']):
            return redirect('/wall')
        else:
            session['logout'] = True
    except:
        pass
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
