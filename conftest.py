import pytest
from main import BooksCollector


@pytest.fixture()
def collector():
    collector = BooksCollector()

    return collector


@pytest.fixture()
def book_name():
    book = 'Дюна'

    return book
