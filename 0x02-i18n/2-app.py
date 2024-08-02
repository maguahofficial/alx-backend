#!/usr/bin/env python3
"""The Basic Flask app, Basic Babel setup, Get locale from request """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" The instantiate the Babel object """


class Config(object):
    """ The config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Function use that class as config for Flask app """


@app.route('/')
def root():
    """ basic function Flask app """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ function to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
