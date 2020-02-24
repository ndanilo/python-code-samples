class ClientList:
    def __init__(self):
        self._clientlist = []

    def add(self, item):
        self._clientlist.append(item)

    def __getitem__(self, position):
        return self._clientlist[position]

    def __str__(self):
        return str(self._clientlist)
            