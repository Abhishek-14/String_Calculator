import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

def test_multiple_numbers_returns_sum():
    assert add("1,2,3") == 6
    assert add("4,5,6,7,8") == 30

def test_newline_or_comma_as_delimiter():
    assert add("1\n2,3") == 6
    assert add("4\n5\n6") == 15

def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//|\n4|5|6") == 15
    assert add("//.\n2.3.4") == 9

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -2"):
        add("1,-2,3")

    with pytest.raises(ValueError, match="negative numbers not allowed: -2, -3"):
        add("//;\n1;-2;-3")
