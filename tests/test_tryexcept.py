from src.item import Item


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 3