from flask import Flask
from flask_sqlalchemy import SQLAlchemy

quotes = Flask(__name__)
quotes.config.from_object('settings/base')
# db = SQLAlchemy(quotes)

from . import app