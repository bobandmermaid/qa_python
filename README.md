## qa_python_sprint_4

### Список реализованных тестов для приложения BooksCollector. Оно позволяет установить жанр книг и добавить их в избранное.
1. test_init_attributes_initial_value - Проверка инициализации атрибутов класса, с заданными по-умолчанию значениями.
2. test_add_new_book_add_two_books - Проверка корректности добавления двух книг в коллекцию.
3. test_add_new_book_empty_name_book - Проверка невозможности добавления пустой строки вместо имени.
4. test_set_book_genre_one_set_not_one_set - Проверка добавления списка жанров установленных по-умолчанию и невозможности добавления жанра не из списка.
5. test_get_book_genre_name_book_genre - Проверка возврата нужного жанра по названию книги.
6. test_get_books_with_specific_genre_returned_specific_genre_books_list - Проверка книг с заданным жанром. Должна быть в списке заданных жанров по-умолчанию.
7. test_get_books_with_specific_genre_invalid_books_genre - Проверка книг с невалидным заданным жанром. Отсутствует в списке задных жанров.
8. test_get_books_for_children_name_returned_books_without_rating - Проверка, что книга для детей, содержится в списке без возрастного рейтинга.
9. test_add_book_in_favorites_name_book_in_favorites - Проверка, что добавленная книга содержится в списке избранных.
10. test_delete_book_from_favorites_name_book_not_in_favorites Проверка, что удаленная книга отсутсвует в списке избранных книг.
