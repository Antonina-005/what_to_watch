# flake8: noqa
# mypy: ignore-errors
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Импорты в самом конце файла
from . import cli_commands, error_handlers, views  # noqa: F401
