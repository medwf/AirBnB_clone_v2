#!/usr/bin/python3
"""this script starts a Flask web application
    this web application must be listening on 0.0.0.0 at port 5000
    Route:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display 'C ', followed by the value of the text variable
            (replace underscore _ symbols with a space )
        /python/<text>: display 'Python ', followed by the value of the text
            variable (replace underscore _ symbols with a space )
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_route(text="is cool"):
    """this methods return python <text> at '/python/<test>' path"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
