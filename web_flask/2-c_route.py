#!/usr/bin/python3
"""Hello Flask!"""
from flask import Flask
from markupsafe import escape

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
def hello_c(text):
    """Show text"""
    t = text.replace("_", " ")
    return f"C {escape(t)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
