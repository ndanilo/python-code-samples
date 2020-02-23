from Models.model import *
from Models.car import Car
from Models.motorcycle import Motorcycle

f = Movie()
f.name = 'avatar o menino do gelo'

print(f.name)

c = Car('Ferrari')
m = Motorcycle('Fazer 250')

print(c.definition())
print(m.definition())


