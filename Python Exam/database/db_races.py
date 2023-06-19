import pyodbc


connection = pyodbc.connect("Driver=SQL Server; Server=NIKS-2700X\SQLEXPRESS; Database=dnd_vault; Trusted_Connection=yes")

class DB_Races:
    def __init__(self):
        pass

    #READ
    def get_races(self):
        cursor = connection.cursor()
        query = f"SELECT * FROM dbo.races"
        cursor.execute(query)
        races_data = []
        for data_row in cursor:
            races_data.append(data_row)
        return races_data

    #CREATE
    def insert_race(self, newRace):
        cursor = connection.cursor()
        query = f"INSERT INTO dbo.races (race, str, dex, con) VALUES (?, ?, ?, ?)"
        values = (newRace.raceName, newRace.strength, newRace.dexterity, newRace.constitution)
        cursor.execute(query, values)
        connection.commit()

    #DELETE
    def delete_race(self, rID):
        cursor = connection.cursor()
        query = f"DELETE FROM dbo.races WHERE rID = '{rID}'"
        cursor.execute(query)
        connection.commit()