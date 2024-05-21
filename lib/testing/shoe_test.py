# lib/testing/shoe_test.py

import pytest
from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", 10)
    assert shoe.brand == "Nike"
    assert shoe.size == 10

def test_shoe_brand_validation():
    with pytest.raises(ValueError):
        shoe = Shoe("", 10)
    with pytest.raises(ValueError):
        shoe = Shoe("a" * 51, 10)

def test_shoe_size_validation():
    with pytest.raises(ValueError):
        shoe = Shoe("Nike", 4)
    with pytest.raises(ValueError):
        shoe = Shoe("Nike", 16)
