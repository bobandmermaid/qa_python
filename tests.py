import pytest


class TestBooksCollector:

    def test_init_attributes_initial_value(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_empty_name_book(self, collector):
        collector.add_new_book('')

        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('genre_and_result', [['Комедии', 'Комедии'], ['Драма', '']])
    def test_set_book_genre_one_set_not_one_set(self, collector, genre_and_result, book_name):
        genre, result = genre_and_result
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        genre_added = collector.get_book_genre(book_name)

        assert genre_added == result

    def test_get_book_genre_name_book_genre(self, collector, book_name):
        collector.add_new_book(book_name)

        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы', 'Фантастика'])
    def test_get_books_with_specific_genre_returned_specific_genre_books_list(self, genre, collector, book_name):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        books = collector.get_books_with_specific_genre(genre)

        assert book_name in books

    @pytest.mark.parametrize('genre', ['Трагедия', 'Драма', 'Миф'])
    def test_get_books_with_specific_genre_invalid_books_genre(self, genre, collector, book_name):
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        books = collector.get_books_with_specific_genre(genre)

        assert book_name not in books

    def test_get_books_for_children_name_returned_books_without_rating(self, collector):
        name = 'Маугли'
        genre = 'Мультфильмы'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books = collector.get_books_for_children()

        assert name in books

    @pytest.mark.parametrize('book', ['Дюна', 'Десять негритят', 'Сияние'])
    def test_add_book_in_favorites_name_book_in_favorites(self, book, collector):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        favorites = collector.get_list_of_favorites_books()

        assert book in favorites

    @pytest.mark.parametrize('book', ['Дюна', 'Десять негритят', 'Сияние'])
    def test_delete_book_from_favorites_name_book_not_in_favorites(self, book, collector):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        favorites = collector.get_list_of_favorites_books()

        assert book not in favorites
