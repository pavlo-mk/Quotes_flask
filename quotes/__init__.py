from flask import Flask

quotes = Flask(__name__)
quotes.config.from_object('base')

from . import app