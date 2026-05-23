import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    return BooksCollector() 

@pytest.fixture
def ten_books_with_different_genres():
    collection = BooksCollector()
    # добавление книг разных жанров
    collection.books_genre = {
        'Дракула': 'Ужасы',
        'Сияние': 'Ужасы',
        'Десять негритят': 'Детектив',
        'Приключения Шерлока Холмса': 'Детектив',
        'Солярис': 'Фантастика',
        'Задача трех тел': 'Фантастика',
        'Ревизор': 'Комедии',
        'Простоквашино': 'Комедии',
        'Чебурашка': 'Мультфильмы',
        'Маленький принц': 'Мультфильмы',
    }
    return collection
   
