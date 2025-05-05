import pytest

from app_test.calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8

def test_add_2():
    assert add(1001, 1002) == 2003

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)