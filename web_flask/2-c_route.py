#!/usr/bin/python3
"""this script starts a Flask web application
    this web application must be listening on 0.0.0.0 at port 5000
    Route:
        "/" : disply "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """this methods return Hello HBNB! at '/' path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this methods return HBNB at '/hbnb' path"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """this methods return C <text> at '/c/<test>' path"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
