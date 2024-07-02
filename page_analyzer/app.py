from page_analyzer.db import create_connection

from flask import Flask
from flask import render_template, request, url_for

from datetime import datetime


app = Flask(__name__)
conn = create_connection()


def is_valid(url):
    return True


def save_data(conn, url):
    with conn.cursor() as curs:
        curs.execute("""INSERT INTO urls (name, created_at) values (%s, %s)""", [url, datetime.now()])
    conn.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/urls", methods = ['POST', 'GET'])
def urls():
    if request.method == "POST":
        # save the data
        url = request.form.get("url")
        save_data(conn, url)
        return render_template("show.html",
                               url=url)
    return render_template("index.html")


