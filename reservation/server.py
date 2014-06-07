#! /usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """hello world"""
    return "Hello World!"

@app.route("/hello/<user>")
def welcome(user):
    """hello world"""
    return "Hello World!", user

if __name__ == "__main__":
    app.run()
