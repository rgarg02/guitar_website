import os

from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Set up database
engine = create_engine("postgres://tkshbzeektlwhv:f209d2aefdc18f0fe5f63f887d1f81699aa11072db1f0d325cee71a31a7ecb36@ec2-18-210-51-239.compute-1.amazonaws.com:5432/d5h8srknfc94e4")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/covers")
def covers():
    return render_template("covers.html")

@app.route("/request")
def request_song():
    return render_template("request.html")

@app.route("/submit", methods=['POST'])
def submit_form():
    email = request.form.get("email")
    song = request.form.get("song_request")
    db.execute("INSERT INTO requests (email,song) VALUES (:a,:b)",{"a":email,"b":song})
    db.commit()
    return render_template("song.html",song=song)
