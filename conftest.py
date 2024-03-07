import pytest

@pytest.fixture(scope='function')
def correct_user_info():
    return {'name': 'Яна', 'login': 'karpova_6125@yandex.ru', 'password': '1234567'}

@pytest.fixture(scope='function')
def incorrect_user_info():
    return {'name': '', 'login': 'karpova_yandex_ru', 'password': '12345'}