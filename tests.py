import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_correct_books_added(self, collection):
        list_of_books = ['а', 'Парфюмер', 'а'*40]
        for book in list_of_books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    @pytest.mark.parametrize('wrong_book_name', ['', 'а'*41, 'а'*50])
    def test_add_new_book_wrong_input_books_not_added(self, collection, wrong_book_name):
        collection.add_new_book(wrong_book_name)
        assert len(collection.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['Сияние', 'Ужасы'],
            ['Десять негритят', 'Детективы'],
            ['Солярис', 'Фантастика'],
            ['Ревизор', 'Комедии'],
            ['Чебурашка', 'Мультфильмы']
        ]
    )
    
    def test_set_book_genre_genre_added(self, collection, book_name, genre):
        collection.add_new_book(book_name)
        collection.set_book_genre(book_name, genre)
        assert collection.get_book_genre(book_name) == genre

    def test_get_book_genre_wrong_genre_not_added(self, collection): 
        collection.add_new_book('Остров сокровищ')
        collection.set_book_genre('Остров сокровищ', 'Приключения')
        assert collection.get_book_genre('Остров сокровищ') == ''

    @pytest.mark.parametrize('specific_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_true(self, ten_books_with_different_genres, specific_genre):
        books_with_specific_genre = ten_books_with_different_genres.get_books_with_specific_genre(specific_genre)
        for book in books_with_specific_genre:
          assert ten_books_with_different_genres.get_book_genre(book) == specific_genre
       
    def test_get_books_genre_true(self, collection):
        collection.add_new_book('Чебурашка')
        collection.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collection.get_books_genre() == {'Чебурашка': 'Мультфильмы'}
        
    def test_get_books_for_children_books_with_age_rating_excluded(self, ten_books_with_different_genres):
        children_books = ten_books_with_different_genres.get_books_for_children()
        for book in children_books:
          genre = ten_books_with_different_genres.get_book_genre(book)
          assert genre not in ten_books_with_different_genres.genre_age_rating

    def test_add_book_in_favorites_book_added(self, collection):
        book_name = 'Ревизор'
        collection.add_new_book(book_name)
        collection.add_book_in_favorites(book_name)
        assert book_name in collection.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_deleted(self, collection):
        book_name = 'Ревизор'
        collection.add_new_book(book_name)
        collection.add_book_in_favorites(book_name)
        collection.delete_book_from_favorites(book_name)
        assert book_name not in collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_correct_list(self, collection):
        list_of_books = ['Сияние', 'Десять негритят', 'Солярис']
        for book in list_of_books:
            collection.add_new_book(book)
            collection.add_book_in_favorites(book)
        collection.add_new_book('Маленький принц')
        assert collection.get_list_of_favorites_books() == ['Сияние', 'Десять негритят', 'Солярис']
        
