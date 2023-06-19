import json

class Export_Json:

    def __init__(self):
        pass

    @staticmethod
    def dict_convert_character(characterData):
        characterDict = {
            'pcID': characterData.pcID,
            'pID': characterData.pID,
            'name': characterData.characterName,
            'race': characterData.raceName,
            'str': characterData.strength,
            'dex': characterData.dexterity,
            'con': characterData.constitution,
            'description': characterData.description
        }
        return characterDict

    @staticmethod
    def export_character(characterDict):

        with open(f"export/{characterDict['name']}.json", 'w') as file:
            json.dump(characterDict, file)
