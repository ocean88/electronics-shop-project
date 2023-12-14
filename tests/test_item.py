"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    item = Item("test", 10, 5)
    assert item.name == "test"
    assert item.price == 10
    assert item.quantity == 5