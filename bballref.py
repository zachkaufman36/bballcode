from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import datetime
import os
import json
import bballdicts
import internetgrabber
from basketball_reference_scraper.teams import get_roster

path = r'C:\Users\zkaufman\Documents\Coding Fun\Random Code\bballcode'
filenames = {}
d = {}
heightcalc = []
date = 0
today = datetime.date.today()
currentyear = (today.year)


# This function returns a player's stats for a given year (function will receive a year input as well)
def playerstatistics(player, date):
    gamestatus = {} # Stores date of game and status
    if player in filenames:
        f = open(f'.\\player_jsons\\{date}\\{player}_{date}.json','r')
        playerstats = json.load(f)

    else:
        client.regular_season_player_box_scores(player_identifier=player, season_end_year=date, output_type = OutputType.JSON, output_file_path = f'{path}\\player_jsons\\{date}\\{player}_{date}.json', include_inactive_games=True)
        f = open(f'.\\player_jsons\\{date}\\{player}_{date}.json','r')
        playerstats = json.load(f)
        filenames.update({player: 1})

    f2 = open(f'{path}\\player_jsons\\{date}\\playerdict_{date}.json','r')
    playerdict = json.load(f2)
    name = playerdict[player]
    #team = playerstats[0]['team'] # <--- ISSUE

    z = 0
    for count, i in enumerate(playerstats):
        if z == 8:
            break
        z += 1
        date = i['date']
        status = i['active']
        team = i['team']
        gamestatus.update({date:[team, status]})
    f.close()   
    f2.close() 
    return(name, gamestatus)

# Puts all player files in a dictionary, that way their existance can be checked. If the file already exists the 
# code can pull from the json file rather than from the internet (lessen the load on the website)
def filefiller(path, date):
    for file in os.listdir(f'{path}\\player_jsons\\{date}'):
        if file.endswith('.json'):
            file, trash = os.path.splitext(file)
            filenames.update({file: 1})

# Checks to see if the date file exists for a user specified date. If it doesn't it is created
def file_existance(path, date):
    existance = os.path.exists(f'{path}\\player_jsons\\{date}')
    if existance == False:
        os.mkdir(f'{path}\\player_jsons\\{date}')


if __name__ == '__main__':
                                                      
    while date > currentyear or date < 1949:
        date = int(input("Please choose a year you would like to pull your data from: "))

    file_existance(path, date)
    filefiller(path, date)
    
    if (f'playerdict_{date}.json') not in os.listdir(f'{path}\\player_jsons\\{date}'):
        internetgrabber.players_of_year(path, date)

    file = open(f'{path}\\player_jsons\\{date}\\playerdict_{date}.json', 'r')
    playerfile = json.load(file)

    x = 0
    for player in playerfile:
        if x == 4:
            break
        x += 1
        nameteamgamestatus = playerstatistics(player, date)
        name = nameteamgamestatus[0]
        #team = nameteamgamestatus[1]
        gamestatus = nameteamgamestatus[1]
        for gamedate in gamestatus:
            team = gamestatus[gamedate][0]
            status = gamestatus[gamedate][1]


        value = bballdicts.teamdict[team]

        if team not in d:
            d.update({team: get_roster(value, date)})

        else:
            pass

        indexvalue = {name: int(d[team].loc[d[team]['PLAYER'] == name].index.values)}
        weight = (d[team]['WEIGHT'].loc[d[team].index[indexvalue[name]]])
        height = (d[team]['HEIGHT'].loc[d[team].index[indexvalue[name]]])
        heightcalc = height.split('-')
        height = int(heightcalc[0]) * 12 + int(heightcalc[1])
        heightcalc.clear()
        playerstuff = {name: [team, weight, height, gamestatus]}
        print(name, playerstuff[name], end = '\n' * 2)
