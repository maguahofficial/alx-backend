#!/usr/bin/env python3
""" The basic flask app, Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" this instantiate the Babel object """


class Config(object):
    """ the config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" function Uses that class as config for Flask app """


@app.route('/')
def root():
    """ basic fanction Flask app """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
