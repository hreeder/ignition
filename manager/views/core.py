from manager import app
from flask import render_template

@app.route("/")
def index():
    render_template("index.html")