class BaseMixin:
    def __init__(self, nome):
        self.__nome = nome

    def showName(self):
        print(self.__nome)

class ClientMixin(BaseMixin):
    def __init__(self, nome):
        super().__init__("Jose")
        self.__nome = nome

    def showName(self):
        super().showName()
        print(self.__nome)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value