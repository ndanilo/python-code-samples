class Item:
    __id = None
    __description = None
    __date = None

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, value):
        self.__id = value

    @property
    def Description(self):
        return self.__description

    @Description.setter
    def Description(self, value):
        self.__description = value

    @property
    def Date(self):
        return self.__date

    @Date.setter
    def Date(self, value):
        self.__date = value

    def to_json(self):
        return {
            'Id':self.Id,
            'Description':self.Description,
            'Date':self.Date.isoformat()
        }

    def __str__(self):
        return f'Id: {self.Id} - Description: {self.Description} - Date: {self.Date}'