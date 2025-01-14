from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Невозможно сложить экземпляр Phone или Item с объектом другого класса")
        return self.quantity + other.quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Phone({repr(self.name)}, {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value not in [1, 2]:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self._number_of_sim = value