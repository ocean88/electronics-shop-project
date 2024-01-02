from src.item import Item


class Mixinlog:

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_language):
        if new_language in ['EN', 'RU']:
            self._language = new_language
        else:
            raise AttributeError("AttributeError: property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, Mixinlog):
    def __init__(self, name: str, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language

    def __str__(self):
        return self.name
