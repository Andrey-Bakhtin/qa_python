import pytest
from books_collector import BooksCollector

class TestBooksCollector:

    def test_add_new_book_valid(self):
        """Тест добавления книги с корректным названием (до 40 символов)"""
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.get_books_genre()
        assert collector.get_book_genre('Война и мир') == ''

    @pytest.mark.parametrize('book_name', [
        '',  # пустая строка
        'a' * 41  # строка длиннее 40 символов
    ])
    def test_add_new_book_invalid_name(self, book_name):
        """Тест добавления книги с некорректным названием (пустое или слишком длинное)"""
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_duplicate_book(self):
        """Тест попытки добавить книгу повторно"""
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Дюна')  # повторная попытка
        assert len(collector.get_books_genre()) == 1
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre', [
        ('1984', 'Фантастика'),
        ('Мастер и Маргарита', 'Мультфильмы'),
        ('Шерлок Холмс', 'Детективы')
    ])
    def test_set_book_genre_valid(self, book_name, genre):
        """Тест установки корректного жанра для существующей книги"""
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre(self):
        """Тест установки несуществующего жанра"""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Нон-фикшн')  # жанра нет в списке
        assert collector.get_book_genre('1984') == ''

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Дюна']),
        ('Ужасы', ['Дракула']),
        ('Детективы', ['Шерлок Холмс'])
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        """Тест получения книг по конкретному жанру"""
        collector = BooksCollector()
        # Добавляем книги с разными жанрами
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_for_children(self):
        """Тест получения книг, подходящих детям (без возрастного рейтинга)"""
        collector = BooksCollector()
        # Книги с возрастным рейтингом (не должны попасть в результат)
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        # Книги без возрастного рейтинга (должны попасть в результат)
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_new_book('Книга без жанра')

        children_books = collector.get_books_for_children()
        assert 'Винни-Пух' in children_books
        assert 'Книга без жанра' in children_books
        assert 'Дракула' not in children_books

    def test_add_and_delete_from_favorites(self):
        """Тест добавления и удаления книги из избранного"""
        collector = BooksCollector()
        collector.add_new_book('1984')

        # Добавление в избранное
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

        # Удаление из избранного
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_add_duplicate_to_favorites(self):
        """Тест попытки добавить одну и ту же книгу в избранное дважды"""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')  # повторная попытка

        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('1984') == 1  # должна быть только одна копия

    def test_get_books_genre_dict(self):
        """Тест получения полного словаря книг с жанрами"""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Мастер и Маргарита')

        expected = {
            '1984': 'Фантастика',
            'Мастер и Маргарита': ''
        }
        assert collector.get_books_genre() == expected
