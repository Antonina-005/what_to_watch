# mypy: ignore-errors
from . import db


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(256), nullable=True)
    # Добавляем недостающее поле для фиксации автора мнения
    added_by = db.Column(db.String(64), nullable=True)
