from src.item import Item


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv('../src/items.csv')
    Item.instantiate_from_csv('../src/item.csv')
