# mypy: ignore-errors
from flask import render_template

from . import db
from .views import opinions_bp


@opinions_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@opinions_bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
