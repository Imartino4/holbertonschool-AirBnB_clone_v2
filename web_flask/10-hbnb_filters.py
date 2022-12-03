#!/usr/bin/python3
"""This modules start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filter")
def show_html(id="None"):
    """Display hbnb web page"""
    from models.state import State
    from models.city import City
    from models.amenity import Amenity

    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    
    return render_template(
        '10-hbnb_filters.html', states=states, cities=cities,
        amenities=amenities)

@app.teardown_appcontext
def teardown(error):
    """remove session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
