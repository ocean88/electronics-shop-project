from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Genius', 9600, 5)
    assert str(kb) == "Genius"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
