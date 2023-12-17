import csv
from typing import List


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def cut_name(self):
        return self._name

    @cut_name.setter
    def cut_name(self, name):
        self._name = name
        if len(self._name) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        return self._name

    @classmethod
    def instantiate_from_csv(cls, source_file: str) -> List:
        """
       проверка на чтение файла
        """
        try:
            with open(source_file, 'r') as file:
                reader = csv.DictReader(file)
                Item.all = [item for item in reader]
                return Item.all
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file '{source_file}' not found.")

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        result = self.price * self.pay_rate
        self.price = round(result)


