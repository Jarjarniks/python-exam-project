from flask import Flask, render_template, request, url_for, redirect
from service.player_character_service import Player_Character_Service, Player_Service
from service.races_service import Races_Service
from service.stats_service import Stats_Service
from service.export_json_service import Export_Json

app = Flask(__name__)

player_characterService = Player_Character_Service()
player_service = Player_Service()
races_service = Races_Service()


@app.route("/")
@app.route("/home")
@app.route("/home/")
def home():
    return render_template('index.html', title="DnD Vault")

###################################################################  PLAYER CHARS  #####################################################################################
#########################################################################################################################################################################

#endpoint for list of all player characters
@app.route('/player-characters')
@app.route('/player-characters/')
def player_characters():
    player_characters = player_characterService.get_player_characters()
    players = player_service.get_players()
    return render_template('player-characters.html', title='Player Characters', chars=player_characters, players=players)

#endpoint for specific player characters
@app.route('/player-characters/<pcID>')
def player_chars_by_pcID(pcID):
    char = player_characterService.get_player_character_by_pcID(pcID)
    if char:
        return render_template('player-character.html', title=char.characterName, char=char)
    else:
        return '<h1>Apologies, a character with that pcID does not exist.</h1>'

#endpoint for creating player characters
@app.route('/create-player-character', methods=["GET", "POST"])
@app.route('/create-player-character/', methods=["GET", "POST"])          
def create_pChar():
    races = races_service.get_races()
    players_list = player_service.get_players()
    if request.method == "POST":
        #Main char info
        playerName = request.form['player-name']
        pID = None
        for p in players_list:
            if p.playerName == playerName:
                pID = p.pID
                break
        characterName = request.form['pchar-name']
        desc = request.form.get('pchar-desc', None)
        #Race section
        chosenRace = request.form['pchar-race']
        raceObj = None
        for race in races:
            if chosenRace == race.raceName:
                raceObj = race
        #Stats section
        strength = int(request.form['pchar-str'])
        dexterity = int(request.form['pchar-dex'])
        constitution = int(request.form['pchar-con'])
        #Service action
        statsObj = Stats_Service.create_stats_obj(strength, dexterity, constitution)
        created_character = player_characterService.create_player_character(pID, characterName, raceObj, statsObj, desc)
        return redirect(url_for('player_chars_by_pcID', pcID=created_character.pcID))
    else:
        return render_template('create-player-char.html', title='Create Character', races=races, players=players_list)

#endpoint for editing player characters
@app.route('/player-characters/<pcID>/edit', methods=["GET", "POST"])
@app.route('/player-characters/<pcID>/edit/', methods=["GET", "POST"])
def update_pChar(pcID):
    races = races_service.get_races()
    players_list = player_service.get_players()
    char = player_characterService.get_player_character_by_pcID(pcID)
    if request.method == "POST":
        playerName = request.form['player-name']
        pID = None
        for p in players_list:
            if p.playerName == playerName:
                pID = p.pID
        newName = request.form['pchar-name']
        newDesc = request.form.get('pchar-desc', None)
        player_characterService.update_player_character(pcID, pID, newName, newDesc)
        return redirect(url_for('player_chars_by_pcID', pcID=pcID))
    else:
        return render_template('edit-player-char.html', char=char, title=char.characterName, races=races, players=players_list)

#endpoint for deleting player characters
@app.route('/player-characters/<pcID>/delete', methods=["POST"])
@app.route('/player-characters/<pcID>/delete/', methods=["POST"])
def delete_pChar(pcID):
    player_characterService.delete_player_character(pcID)
    return redirect(url_for("home"))

#endpoint for exporting player characters
@app.route('/player-characters/<pcID>/export', methods=["GET", "POST"])
def export_pChar(pcID):
    character_data = player_characterService.get_player_character_by_pcID(pcID)
    characterDict = Export_Json.dict_convert_character(character_data)
    Export_Json.export_character(characterDict)
    return render_template("index.html")

###################################################################  PLAYERS  ###########################################################################################
#########################################################################################################################################################################

#endpoint for list of players
@app.route('/players', methods=["GET", "POST"])
@app.route('/players/', methods=["GET", "POST"])
def players():
    players_list = player_service.get_players()
    if request.method == "POST":
        playerName = request.form['player-name']
        email = request.form['player-email']
        player_service.create_player(playerName, email)
        return redirect(url_for('players', title='Players', players=players_list))
    else:
        return render_template('players.html', title='Players', players=players_list)

#endpoint for specific player and a list of their characters
@app.route('/players/<pID>', methods=["GET", "POST"])
@app.route('/players/<pID>/', methods=["GET", "POST"])
def players_by_pID(pID):
    player = player_service.get_player_by_pID(pID)
    player_chars_list = player_service.get_a_players_chars(pID)
    if request.method == "POST":
        name = request.form['player-name']
        email = request.form['player-email']
        player_service.update_player(pID, name, email)
        return redirect(url_for('players'))
    else:
        return render_template('player.html', title=player.playerName, player=player, chars=player_chars_list)

#endpoint for deleting player
@app.route('/players/<pID>/delete', methods=["POST"])
def delete_player(pID):
    pID = request.form['pID']
    player_service.delete_player(pID)
    return redirect(url_for('home'))

#####################################################################  Races  ###########################################################################################
#########################################################################################################################################################################

#endpoint for list of races
@app.route('/races')
@app.route('/races/')
def races():
    race_list = races_service.get_races()
    return render_template('races.html', title='Races', races=race_list)

#endpoint for creating race
@app.route('/races/create', methods=["GET", "POST"])
@app.route('/races/create/', methods=["GET", "POST"])
def create_race():
    if request.method == "POST":
        race = request.form['race']
        str = request.form['race-str']
        dex = request.form['race-dex']
        con = request.form['race-con']
        races_service.create_race(race, str, dex, con)
        return redirect(url_for('races'))
    else:
        return render_template('create-race.html', title='Create Race')

#endpoint for deleting race
@app.route('/races/delete', methods=["POST"])
def delete_race():
    rID = int(request.form['rID'])
    races_service.delete_race(rID)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)