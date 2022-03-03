from select import select
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',status=True)

@app.route('/home')
def home():
    username = request.args.get('uname')
    password = request.args.get('pass')

    connection = sqlite3.connect('vasu.db')
    con = connection.cursor()

    users = list(con.execute('select * from users'))

    con.close()
    connection.close()

    for user in users:
        if user[1] == username and user[2] == password:
            return render_template('home.html')
    return render_template('index.html',status=False)

@app.route('/next')
def next():
    connection = sqlite3.connect('vasu.db')
    con = connection.cursor()
    
    details = list(con.execute('select * from details'))
    con.close()
    connection.close()

    return render_template('next.html',details=details)

if __name__ == '__main__':
    app.run(debug=True)
