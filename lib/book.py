# lib/book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 100:
            self._title = value
        else:
            raise ValueError("Title must be a string between 1 and 100 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 100:
            self._author = value
        else:
            raise ValueError("Author must be a string between 1 and 100 characters.")
