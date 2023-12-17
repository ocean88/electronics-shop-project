"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item() -> None:
    item = Item("test", 10, 5)
    assert item.name == "test"
    assert item.price == 10
    assert item.quantity == 5


def test_calculate_total_price() -> None:
    item = Item("test", 100, 5)
    assert item.calculate_total_price() == 500


def test_apply_discount() -> None:
    item = Item("test", 500, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 400

