#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.amenity import Amenity
from models.state import State
from models.city import City
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def closing(self):
    """ Close current SQLAlchemy Session """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Display a HTML page like 6-index.html, which was done during
            the project 0x01. AirBnB clone - Web static """
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
