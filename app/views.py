from datetime import datetime

from flask import Flask, render_template, request

from . import app


@app.route("/")
def home():
    remote_addr = dict(remote_addr=request.remote_addr)
    headers = {**remote_addr, **request.headers}
    return render_template("home.html", data=headers)


