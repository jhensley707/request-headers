from datetime import datetime

from flask import Flask, render_template, request

from . import app


@app.route("/")
def home():
    return render_template("home.html", data=request.headers)


