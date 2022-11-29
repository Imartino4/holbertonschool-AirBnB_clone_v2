#!/usr/bin/python3
"""This modules start a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb2():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def show_C(text):
    """Show text"""
    t = text.replace("_", " ")
    return "C {}".format(t)


@app.route("/python/<text>")
@app.route("/python")  # pongo las dos posibles rutas
def show_python(text="is_cool"):
    """Show text python"""
    t = text.replace("_", " ")
    return "Python {}".format(t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
