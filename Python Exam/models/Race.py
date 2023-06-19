class Race:

    def __init__(self, rID, raceName, strength, dexterity, constitution):
        self.__rID = rID
        self.__raceName = raceName
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constitution = constitution
        
    @property
    def rID(self):
        return self.__rID

    @property
    def raceName(self):
        return self.__raceName

    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, newStrength):
        self.__strength += newStrength

    @property
    def dexterity(self):
        return self.__dexterity
    @dexterity.setter
    def dexterity(self, newDexterity):
        self.__dexterity += newDexterity

    @property
    def constitution(self):
        return self.__constitution
    @constitution.setter
    def constitution(self, newConstitution):
        self.__constitution += newConstitution

    def __repr__(self):
        return f"race: {self.raceName} str: {self.strength} dex: {self.dexterity} con: {self.constitution}"