import pytest

from run import app  # Импортируем ваше Flask-приложение из файла run.py


@pytest.fixture
def client():
    # Настраиваем Flask для режима тестирования
    app.config['TESTING'] = True
    # Создаем тестового клиента, который умеет "ходить" по ссылкам сайта
    with app.test_client() as client:
        yield client

def test_main_page_loading(client):
    """Тест проверяет, что главная страница http://127.0.0.1:5000/ открывается без ошибок"""
    response = client.get('/')
    
    # HTTP-статус 200 означает "ОК" (страница успешно загрузилась)
    assert response.status_code == 200
