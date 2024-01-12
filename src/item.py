import csv
from typing import List


class ShellScriptError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта'

    def __str__(self):
        return self.message


class InstantiateCSVError(ShellScriptError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'


class ShellScript:

    def __init__(self, source_file: str) -> None:
        if not source_file:
            raise FileNotFoundError('Отсутствует файл item.csv')

        with open(source_file, 'r') as file:
            items = []
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    raise InstantiateCSVError("CSV файл должен содержать 3 столбца. Файл item.csv поврежден")
                name = row[0]
                items.append(name)

        self.source_file = source_file


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.__name) > 10:
            return self.__name[:10]
        return self.__name

    @staticmethod
    def instantiate_from_csv(source_file: str) -> List[str]:
        items = []
        try:
            ShellScript(source_file)
            return items
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print("Файл item.csv поврежден")


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
