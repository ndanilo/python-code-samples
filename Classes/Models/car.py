from Models.vehicle import *
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self._model = 'car'

    def __str__(self):
        return f'{self._model} - {super().name}'