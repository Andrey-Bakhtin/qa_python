# qa_python
Краткое описание тестов:
    test_add_new_book_valid — проверка добавления книги с корректным именем.
    test_add_new_book_invalid_name (с параметризацией) — проверка граничных случаев (пустая строка и слишком длинное имя).
    test_add_duplicate_book — проверка, что дубликат книги не добавляется.
    test_set_book_genre_valid (с параметризацией) — установка корректных жанров для существующих книг.
    test_set_book_genre_invalid_genre — проверка, что недопустимый жанр не устанавливается.
    test_get_books_with_specific_genre (с параметризацией) — получение книг по жанру.
    test_get_books_for_children — фильтрация книг для детей (без возрастного рейтинга).
    test_add_and_delete_from_favorites — полный цикл: добавление и удаление из избранного.
    test_add_duplicate_to_favorites — проверка, что книга не дублируется в избранном.
    test_get_books_genre_dict — получение полного словаря книг и жанров.
