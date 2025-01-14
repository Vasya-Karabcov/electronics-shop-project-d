from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, count_sim):
        super().__init__(name, price, quantity)
        self.__count_sim = count_sim

    def __repr__(self):
        return f'{self.__class__.__name__}{(self.name, self.price, self.quantity, self.__count_sim)}'

    @property
    def number_of_sim(self):
        return self.__count_sim

    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        if not isinstance(num_sim, int):
            print('Количество физических SIM-карт должно быть целым числом')
        if num_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом и больше нуля')
