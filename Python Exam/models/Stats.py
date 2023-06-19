class Stats:
    def __init__(self, strength, dexterity, constitution):
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constitution = constitution

    @property
    def strength(self):
        return self.__strength

    @property
    def dexterity(self):
        return self.__dexterity
    
    @property
    def constitution(self):
        return self.__constitution

    def __repr__(self):
        return f"RollStr: {self.__strength}, RollDex: {self.__dexterity}, RollCon: {self.__constitution}"