import pyodbc

connection = pyodbc.connect("Driver=SQL Server; Server=NIKS-2700X\SQLEXPRESS; Database=dnd_vault; Trusted_Connection=yes")

##################################################################### PLAYER CHARACTERS  ##################################################################################
###########################################################################################################################################################################

class DB_Player_Characters:
    def __init__(self):
        pass
    
    #READ
    def get_player_characters(self):
        cursor = connection.cursor()
        query = "SELECT * FROM dbo.player_characters"
        cursor.execute(query)
        player_chars_data = []
        for data_row in cursor:
            player_chars_data.append(data_row)
        cursor.close()
        return player_chars_data
    
    def get_player_character_by_pcID(self, pcID):
        cursor = connection.cursor()
        query = "SELECT * FROM dbo.player_characters WHERE pcID=?"
        cursor.execute(query, pcID)
        player_char_data = cursor.fetchone()
        cursor.close()
        return player_char_data
    
    # #CREATE
    def insert_player_character(self, newChar):
        cursor = connection.cursor()
        query = "INSERT INTO dbo.player_characters (pID, characterName, raceName, strength, dexterity, constitution, description) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (newChar.pID, newChar.characterName, newChar.raceName, newChar.strength, newChar.dexterity, newChar.constitution, newChar.description)
        cursor.execute(query, values)
        connection.commit()

        # returns pcID of the created character
        cursor.execute('SELECT @@IDENTITY AS ID')
        pcID = cursor.fetchall()[0][0]
        return pcID
        
    # #UPDATE
    def update_player_character(self, pcID, pID, characterName, desc):
        cursor = connection.cursor()
        query = f"""UPDATE dbo.player_characters 
                SET characterName = ?,
                pID = ?, 
                description = ?
                WHERE pcID = ?"""
        values = (characterName, pID, desc, pcID)
        cursor.execute(query, values)
        connection.commit()

    #DELETE
    def delete_player_character(self, pcID):
        cursor = connection.cursor()
        query = f"DELETE FROM dbo.player_characters WHERE pcID = {pcID}"
        cursor.execute(query)
        connection.commit()

#########################################################################  PLAYERS  #######################################################################################
###########################################################################################################################################################################

class DB_Players:
    def __init__(self):
        pass

    #READ
    def get_players(self):
        cursor = connection.cursor()
        query = f"SELECT * FROM dbo.players"
        cursor.execute(query)
        players_data = []
        for datarow in cursor:
            players_data.append(datarow)
        cursor.close()
        return players_data

    def get_player_by_pID(self, pID):
        cursor = connection.cursor()
        query = f"SELECT * FROM dbo.players WHERE pID = {pID}"
        cursor.execute(query)
        player_data = cursor.fetchone()
        cursor.close()
        return player_data
    
    def get_a_players_chars(self, pID):
        cursor = connection.cursor()
        query = f"""SELECT * FROM dbo.player_characters
                WHERE pID = '{pID}'"""
        cursor.execute(query)
        players_chars_data = []
        for data_row in cursor:
            players_chars_data.append(data_row)
        return players_chars_data
    
    # #CREATE
    def insert_player(self, newPlayer):
        cursor = connection.cursor()
        query = f"INSERT INTO dbo.players (name, email) VALUES (?, ?)"
        values = (newPlayer.playerName, newPlayer.email)
        cursor.execute(query, values)
        connection.commit()

    # #UPDATE
    def update_player(self, pID, name, email):
        cursor = connection.cursor()
        query = f"""UPDATE dbo.players SET name = '{name}',
                email = '{email}' 
                WHERE pID = '{pID}'"""
        cursor.execute(query)
        connection.commit()

    # #DELETE
    def delete_player(self, pID):
        cursor = connection.cursor()
        query = f"DELETE FROM dbo.players WHERE pID = {pID}"
        cursor.execute(query)
        connection.commit()
