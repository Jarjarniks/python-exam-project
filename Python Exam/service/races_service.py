from database.db_races import DB_Races
from models.Race import Race

class Races_Service:
    def __init__(self):
        self.__db_races = DB_Races()

    def get_races(self):
        races_data = self.__db_races.get_races()
        races = []
        for data in races_data:
            newRace = Race(*data)
            races.append(newRace)
        return races
    
    def create_race(self, race, str, dex, con):
        newRace = Race(None, race, str, dex, con)
        self.__db_races.insert_race(newRace)

    def delete_race(self, rID):
        self.__db_races.delete_race(rID)