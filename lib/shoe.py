# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 50:
            self._brand = value
        else:
            raise ValueError("Brand must be a string between 1 and 50 characters.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) and 5 <= value <= 15:
            self._size = value
        else:
            raise ValueError("Size must be a number between 5 and 15.")
