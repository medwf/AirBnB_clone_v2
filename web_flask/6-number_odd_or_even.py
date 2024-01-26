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
        /number/<n>: display 'n is a number' only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: 'Number: n' inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """this methods return <n> is a number at '/number/<n>' path"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """this methods return template with variable n
    at '/number_template/<n>' path
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """this methods return template with variable result
        that sheck if n is odd or even.
        at '/number_odd_or_even/<n>' path
    """
    if n % 2 == 0:
        result = f"{n} is even"
    else:
        result = f"{n} is odd"
    return render_template('6-number_odd_or_even.html', result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
