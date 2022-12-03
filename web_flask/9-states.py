#!/usr/bin/python3
"""This modules start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def show_html(id="None"):
    """Display states list in order
    *check_id = 1 when id is correct
    """
    from models.state import State
    from models.city import City

    states = storage.all(State).values()
    cities = storage.all(City).values()
    check_id = 0
    s_id = id
    for s in states:
        if s_id == s.id:
            check_id = 1
            s_id = id
            break
    return render_template(
        '9-states.html', states=states, cities=cities,
        s_id=s_id, check_id=check_id)


@app.teardown_appcontext
def teardown(error):
    """remove session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
