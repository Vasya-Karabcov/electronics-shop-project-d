import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден.'

    def __str__(self):
        return self.message

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

    def __repr__(self):
        return f'{self.__class__.__name__}{(self.__name, self.price, self.quantity)}'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            return print("Длина превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        Item.all.clear()
        file = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(file):
            raise FileNotFoundError('Отсутствует файл item.csv')

        with open(file, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames == [
                "name",
                "price",
                "quantity",
            ]:
                raise InstantiateCSVError
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(str_num):
        str_num = float(str_num)
        return int(str_num)

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
        self.price *= self.pay_rate


