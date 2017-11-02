import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


DEBUG = True


WTF_CSRF_ENABLED = True
SECRET_KEY = 'lhflkk24hflk24jlfk4l25kfh4lk5hfl45khf'


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'quotes.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True