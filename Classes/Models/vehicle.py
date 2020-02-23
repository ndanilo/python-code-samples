class Vehicle:
    def __init__(self, name):
        self._name = name.title()

    @property
    def name(self):
        return self._name