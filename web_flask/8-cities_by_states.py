#!/usr/bin/python3
"""This modules start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def show_html():
    """Display states list in order"""
    from models.state import State
    from models.city import City


    states = storage.all(State).values()
    # if getenv("HBNB_TYPE_STORAGE") == 'db':
    cities = storage.all(City).values()
    return render_template(
        '8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown(error):
    """ """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
