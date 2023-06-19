from database.db_pcs import DB_Player_Characters, DB_Players
from models.PlayerChar import PlayerChar
from models.Player import Player
from service.stats_service import Stats_Service

class Player_Character_Service:

    def __init__(self):
        self.__db_player_characters = DB_Player_Characters()

    def get_player_characters(self):
        player_chars_data = self.__db_player_characters.get_player_characters()
        player_characters = []
        for data in player_chars_data:
            player_characters.append(data)
        return player_characters
    
    def get_player_character_by_pcID(self, pcID):
        player_char_data = self.__db_player_characters.get_player_character_by_pcID(pcID)
        return player_char_data
    
    def create_player_character(self, pID, characterName, raceObj, statsObj, desc):
        raceObj = Stats_Service.calculate_final_stats(raceObj, statsObj)
        newChar = PlayerChar(None, pID, characterName, raceObj, desc)
        pcID = self.__db_player_characters.insert_player_character(newChar)
        created_character = self.__db_player_characters.get_player_character_by_pcID(pcID)
        return created_character
    
    def update_player_character(self, pcID, pID, characterName, desc):
        self.__db_player_characters.update_player_character(pcID, pID, characterName, desc)

    def delete_player_character(self, pcID):
        self.__db_player_characters.delete_player_character(pcID)
    
##########################################################################  Player Service  ###############################################################################
###########################################################################################################################################################################

class Player_Service:

    def __init__(self):
        self.__db_players = DB_Players()

    def get_players(self):
        players_data = self.__db_players.get_players()
        players = []
        for data in players_data:
            newPlayer = Player(*data)
            players.append(newPlayer)
        return players
    
    def get_player_by_pID(self, pID):
        player_data = self.__db_players.get_player_by_pID(pID)
        player = Player(*player_data)
        return player
    
    def get_a_players_chars(self, pID):
        player_chars_data = self.__db_players.get_a_players_chars(pID)
        player_characters = []
        for data in player_chars_data:
            player_characters.append(data)
        return player_characters
    
    def create_player(self, playerName, email):
        newPlayer = Player(None, playerName, email)
        self.__db_players.insert_player(newPlayer)

    def update_player(self, pID, name, email):
        self.__db_players.update_player(pID, name, email)

    def delete_player(self, pID):
        self.__db_players.delete_player(pID)