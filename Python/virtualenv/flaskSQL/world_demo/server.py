from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "df8928&#hu#ihu#8@89h9u$%N%)(8Db!"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'world')


@app.route('/')
def index():
    countries = mysql.query_db("SELECT * FROM countries LIMIT 12")
    return render_template('index.html', countries=countries)

app.run(debug=True)