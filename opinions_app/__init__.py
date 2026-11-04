# mypy: ignore-errors
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Сначала импортируем обработчики и вьюхи для Blueprint
    from . import error_handlers  # noqa: F401
    from .views import opinions_bp
    
    # Регистрируем Blueprint в приложении
    app.register_blueprint(opinions_bp)
    
    # Регистрируем CLI-команду напрямую в приложение app
    from .cli_commands import register_cli_commands
    register_cli_commands(app)
        
    return app