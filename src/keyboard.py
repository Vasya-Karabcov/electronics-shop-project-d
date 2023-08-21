from src.item import Item


class MixinLog:
    '''Вспомогательный клас в вкотором реализуеться смена расскладки'''

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLog, Item):
    pass
