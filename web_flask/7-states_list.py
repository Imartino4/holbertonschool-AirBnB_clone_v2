#!/usr/bin/python3
"""This modules start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def show_html():
    """Display states list in order"""
    from models.state import State
    
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)
    # en html puedo usar states


@app.teardown_appcontext
def teardown(error):
    """ """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)