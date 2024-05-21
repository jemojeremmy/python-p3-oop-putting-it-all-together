# lib/testing/book_test.py

import pytest
from lib.book import Book

def test_book_initialization():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"

def test_book_title_validation():
    with pytest.raises(ValueError):
        book = Book("", "F. Scott Fitzgerald")
    with pytest.raises(ValueError):
        book = Book("a" * 101, "F. Scott Fitzgerald")

def test_book_author_validation():
    with pytest.raises(ValueError):
        book = Book("The Great Gatsby", "")
    with pytest.raises(ValueError):
        book = Book("The Great Gatsby", "a" * 101)
