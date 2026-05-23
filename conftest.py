import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    return BooksCollector() 

@pytest.fixture
def ten_books_with_different_genres():
    collection = BooksCollector()
    
    # добавление книг разных жанров
    collection.add_new_book('Дракула') # ужасы
    collection.add_new_book('Сияние') # ужасы
    collection.add_new_book('Десять негритят') # детективы
    collection.add_new_book('Приключения Шерлока Холмса') # детективы
    collection.add_new_book('Солярис') # фантастика
    collection.add_new_book('Задача трех тел') # фантастика
    collection.add_new_book('Ревизор') # комедии
    collection.add_new_book('Простоквашино') # комедии
    collection.add_new_book('Чебурашка') # мультфильмы
    collection.add_new_book('Маленький принц') # мультфильмы
   
    # установка жанров
    collection.set_book_genre('Дракула', 'Ужасы')
    collection.set_book_genre('Сияние', 'Ужасы')
    collection.set_book_genre('Десять негритят', 'Детективы')
    collection.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
    collection.set_book_genre('Солярис', 'Фантастика')
    collection.set_book_genre('Задача трех тел', 'Фантастика')
    collection.set_book_genre('Ревизор', 'Комедии')
    collection.set_book_genre('Простоквашино', 'Комедии')
    collection.set_book_genre('Чебурашка', 'Мультфильмы')
    collection.set_book_genre('Маленький принц', 'Мультфильмы')
    return collection
