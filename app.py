from flask import Flask, request, render_template, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection, init_db
import random, string

app = Flask(__name__)


init_db()


def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        custom_code = request.form.get('custom_code')
        user_id = session.get('user_id')

        conn = get_db_connection()
        cursor = conn.cursor()

        if custom_code:
            cursor.execute("SELECT * FROM urls WHERE short_code = ?",
                           (custom_code, ))
            if cursor.fetchone():
                flash('Custom short URL already taken.')
                return redirect('/')
            short_code = custom_code
        else:
            while True:
                short_code = generate_short_code()
                cursor.execute("SELECT * FROM urls WHERE short_code = ?",
                               (short_code, ))
                if not cursor.fetchone():
                    break

        cursor.execute(
            "INSERT INTO urls (original_url, short_code, user_id) VALUES (?, ?, ?)",
            (original_url, short_code, user_id))
        conn.commit()
        conn.close()
        return render_template('index.html',
                               short_url=request.host_url + short_code)
    return render_template('index.html')


@app.route('/<short_code>')
def redirect_url(short_code):
    conn = get_db_connection()
    url = conn.execute("SELECT original_url FROM urls WHERE short_code = ?",
                       (short_code, )).fetchone()
    conn.close()
    if url:
        return redirect(url['original_url'])
    return "URL not found", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?",
                            (username, )).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])
    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                     (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        flash('Username already taken')
        return redirect('/login')
    conn.close()
    flash('Registration successful! Please log in.')
    return redirect('/login')

app.run(debug=True)
