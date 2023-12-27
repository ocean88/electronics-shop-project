from src.phone import Phone


def test_phone_add_phone():
    phone1 = Phone("iPhone", 1000, 5, 2)
    phone2 = Phone("Samsung", 800, 3, 1)

    result = phone1 + phone2

    assert result == 8


def test_phone_add_invalid_object():
    phone = Phone("iPhone", 1000, 5, 2)
    other_object = "Invalid Object"

    try:
        phone + other_object
    except TypeError as e:
        assert str(e) == "Невозможно сложить экземпляр Phone или Item с объектом другого класса"