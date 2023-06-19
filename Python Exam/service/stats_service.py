from models.Stats import Stats

class Stats_Service:
    def __init__(self):
        pass

    @staticmethod    
    def create_stats_obj(strength, dexterity, constitution):
        return Stats(strength, dexterity, constitution)

    @staticmethod
    def calculate_final_stats(raceObj, statsObj):
        raceObj.strength = statsObj.strength
        raceObj.dexterity = statsObj.dexterity
        raceObj.constitution = statsObj.constitution
        return raceObj