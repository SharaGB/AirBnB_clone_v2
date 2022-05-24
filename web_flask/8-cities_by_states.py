#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """ Close current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a HTML page """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
