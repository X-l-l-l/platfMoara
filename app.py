import re
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import sqlite3
from credentials import Credentials

app = Flask(__name__)

app.secret_key = "key"
app.database = "sample.db"

credentials = Credentials()
credentials.add_cred("rares", "1234")
credentials.add_cred("admin", "admin")


def connect():
    conn = None
    try:
        conn = sqlite3.connect(app.database)
    except:
        print("Error")
    return conn


def get_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabs = cursor.fetchall()
    final_list = []
    for tab in tabs:
        for t in tab:
            final_list.append(t.replace("(", "").replace(")", "").replace(",", ""))
    return final_list


def get_data(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")

    rows = cur.fetchall()
    headings = list(map(lambda x: x[0], cur.description))

    return headings, rows


def table_choice():
    if request.method == 'POST':
        if request.form['submit_button'] == 'posts':
            return "posts"
        elif request.form['submit_button'] == 'items':
            return "items"
        elif request.form['submit_button'] == 'locations':
            return "locations"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in')
            return redirect(url_for('login'))

    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not credentials.check_cred(request.form['username'], request.form['password']):
            # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash(f"Login successful")
            return redirect(url_for('tables'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Logout successful')
    return redirect(url_for('login'))


table = ""


@app.route('/tables', methods=['GET', 'POST'])
@login_required
def tables():
    table_list = get_tables(connect())
    global table
    if request.method == "POST":
        if request.form.get('posts'):
            table = "posts"
        if request.form.get('items'):
            table = "items"
        if request.form.get('locations'):
            table = "locations"
        return redirect(url_for('table_view'))
    return render_template('list.html', table_list=table_list)


@app.route('/table_view')
@login_required
def table_view():
    conn = connect()
    headings, data = get_data(conn, table)
    return render_template('table.html', headings=headings, data=data)


if __name__ == '__main__':
    app.run(debug=True)