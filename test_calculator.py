import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

