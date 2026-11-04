# mypy: ignore-errors
# what_to_watch/settings.py
import os


class Config(object):  # noqa: UP004
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'MY_SECRET_KEY')
