from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import sqlite3
from werkzeug import exceptions
from controllers import urls
import string
import random

# Hashids is a small open-source library that generates short, unique, non-sequential ids from numbers. It converts numbers like 347 into strings like “yr8”
# alternative to Hashids would be bycrypt

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the URL shortener app'})

def shorten_url():
    conn = get_db_connection()
    while True:
        rand_letters = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        short_url = conn.execute("SELECT shortened FROM urls WHERE shortened = ?", (rand_letters,)).fetchone()
        if not short_url:
            return rand_letters


@app.route('/urls', methods = ['GET', 'POST'])
def home():
    conn = get_db_connection()
    if request.method == 'POST':
        url_to_shorten = request.form['url']
        found_url_obj = conn.execute("SELECT shortened_url FROM urls WHERE original_url = ?", (url_to_shorten,)).fetchone()
        if found_url_obj:
            found_url = found_url_obj[0]
            return redirect(url_for("display_result", url=found_url))
        else:
            short_url = shorten_url()
            conn.execute("INSERT INTO urls (normal, shortened) VALUES (?,?) RETURNING *", (url_to_shorten, short_url)).fetchall()
            conn.commit()
            conn.close()
            return redirect(url_for("display_result", url=short_url))
    else:
        return redirect('http://127.0.0.1:5500/client/index.html')

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)