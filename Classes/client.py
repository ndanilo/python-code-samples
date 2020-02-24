from Models.model import *
from Models.car import Car
from Models.motorcycle import Motorcycle
from Models.clientlist import ClientList

f = Movie()
f.name = 'avatar o menino do gelo'

print(f.name)

c = Car('Ferrari')
m = Motorcycle('Fazer 250')

print(c)
print(m)

clients = ClientList()
clients.add('João')
clients.add('Amanda')
clients.add('Gustavo')
clients.add('Joice')
clients.add('Felipe')

print(clients)


