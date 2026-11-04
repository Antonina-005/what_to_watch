# mypy: ignore-errors
import csv

from . import app, db
from .models import Opinion


@app.cli.command('load-opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    print(f'Загружено мнений: {counter}')
