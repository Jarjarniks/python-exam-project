class Player():
    
    def __init__(self, pID, playerName, email):
        self.__pID = pID
        self.__playerName = playerName
        self.__email = email

    @property
    def pID(self):
        return self.__pID
    
    @property
    def playerName(self):
        return self.__playerName
    @playerName.setter
    def playerName(self, newName):
        self.__playerName = newName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, newEmail):
        self.__email = newEmail

    def __repr__(self):
        return f'pID: {self.pID}, name: {self.playerName}, email: {self.email}'
    
    