#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Display “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display “HBNB” """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space) """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """ Display “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space) """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display “n is a number” only if n is an integer """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
