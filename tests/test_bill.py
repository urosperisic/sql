import pytest

from app_test.bill import Bill


def test_add_single_item():
    b = Bill()
    b.add_item("Bread", 1.5)
    assert b.total() == 1.5
    assert b.item_count() == 1
    assert b.display() == [("Bread", 1.5)]


def test_add_multiple_items():
    b = Bill()
    b.add_item("Milk", 1.0)
    b.add_item("Cheese", 2.5)
    assert b.total() == 3.5
    assert b.item_count() == 2


def test_negative_price_raises_exception():
    b = Bill()
    with pytest.raises(ValueError):
        b.add_item("BadItem", -5)