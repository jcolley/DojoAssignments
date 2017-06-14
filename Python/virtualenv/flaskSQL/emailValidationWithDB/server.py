from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "krhre*#*(#ui3492@pOEIfj!"
mysql = MySQLConnector(app, 'emailvalid')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emails', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
        # We'll then create a dictionary of data from the POST data received.

        data = {
            'email': request.form['email']
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/success')

    return redirect('/')


@app.route('/success')
def success():
    # define your query
    query = "SELECT id, email, DATE(created_at) AS created_at FROM emails"
    # run query with query_db()
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)


@app.route('/remove_email/<email_id>', methods=['POST'])
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')


app.run(debug=True)
