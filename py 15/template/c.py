from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor
    cursor.execute(''' CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close

    @app.route('/')
    def index():
        return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method =='POST' and 'userame' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connection.connect(
            host="remotemysql.com",
            user="Rz8hqn1dK4",
            password="nd0WK03xe0",
            database="Rz8hqn1dK4"
        )

        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = % AND Password',(username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id =account[0]
            msg='Logged in Successfully'
            print('login successfull')
            return render_template('index.html',msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. CHECK NOW'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')