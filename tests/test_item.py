"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item() -> None:
    item = Item("test", 10, 5)
    assert item._name == "test"
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


def test_string_to_number() -> None:
    assert Item.string_to_number("10") == 10
    assert Item.string_to_number("10.5") == 10


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_cut_name() -> None:
    item = Item('Телефон', 10000, 5)
    item.cut_name = 'Смартфон'
    assert item.cut_name == 'Смартфон'

    try:
        item.cut_name = 'СуперСмартфон'
    except ValueError as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."

