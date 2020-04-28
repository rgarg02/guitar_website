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
engine = create_engine("postgresql://rishigarg:iamafreak123@rishigarg-db-web.ci4m0utla2zy.ap-south-1.rds.amazonaws.com:5432/guitarsongs")
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
