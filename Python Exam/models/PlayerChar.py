class PlayerChar:

    def __init__(self, pcID, pID, characterName, raceObj, description=None):
        self.__pcID = pcID
        self.__pID = pID
        self.__characterName = characterName
        self.__raceName = raceObj.raceName
        self.__description = description
        self.__strength = raceObj.strength
        self.__dexterity = raceObj.dexterity
        self.__constitution = raceObj.constitution

    #GENERAL INFO
    @property
    def pcID(self):
        return self.__pcID
    
    @property
    def pID(self):
        return self.__pID
    @pID.setter
    def pID(self, newpID):
        self.__pID = newpID

    @property
    def characterName(self):
        return self.__characterName
    @characterName.setter
    def characterName(self, newName):
        self.__characterName = newName

    @property
    def raceName(self):
        return self.__raceName
    
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, newDesc):
        self.__description = newDesc if newDesc is not None else ''
    
    #STATS
    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, newStrength):
        self.__strength = newStrength

    @property
    def dexterity(self):
        return self.__dexterity
    @dexterity.setter
    def dexterity(self, newDexterity):
        self.__dexterity = newDexterity
    
    @property
    def constitution(self):
        return self.__constitution
    @constitution.setter
    def constitution(self, newConstitution):
        self.__constitution = newConstitution
        

    def __repr__(self):
        return f"""pcID: {self.pcID}, pID: {self.pID}, 
        name: {self.characterName}, race: {self.raceName}, 
        description: {self.description}, str: {self.__strength}
        dex: {self.__dexterity}, con: {self.__constitution}"""
    