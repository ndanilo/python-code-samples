from Models.vehicle import *
class Motorcycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self._model = 'motorcycle'

    def definition(self):
        return f'{self._model} - {super().name}'