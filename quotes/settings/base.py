import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# SECRET_KEY = 'i34brkl23bh4tp'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'quotes.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
