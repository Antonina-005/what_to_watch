import os


class Config(object):  # noqa: UP004
    # Пытаемся взять путь к БД из переменной окружения, если её нет — ставим sqlite по умолчанию
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    # Секретный ключ подтягиваем из скрытого файла .env
    SECRET_KEY = os.getenv('SECRET_KEY', 'MY_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
