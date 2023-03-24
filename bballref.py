from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import datetime
import os
import json
import bballdicts # Needs references to older non-existant teams to exist, otherwise, breaks
import internetgrabber
import sqlfiller
import sqlite3
import time
from basketball_reference_scraper.teams import get_roster

#path = r'C:\Users\zkaufman\Documents\Coding Fun\Random Code\bballcode'
path = r'/mnt/c/users/baker/documents/bballrefcode/bballcode'
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
        f = open(f'./player_jsons/{date}/{player}_{date}.json','r')
        playerstats = json.load(f)

    else:
        client.regular_season_player_box_scores(player_identifier=player, season_end_year=date, output_type = OutputType.JSON, output_file_path = f'{path}/player_jsons/{date}/{player}_{date}.json', include_inactive_games=True)
        print('This should only happen once')
        f = open(f'./player_jsons/{date}/{player}_{date}.json','r')
        playerstats = json.load(f)
        filenames.update({player: 1})

    f2 = open(f'{path}/player_jsons/{date}/playerdict_{date}.json','r')
    playerdict = json.load(f2)
    name = playerdict[player]

    for count, i in enumerate(playerstats):
        date = i['date']
        status = i['active']
        if status == True:
            status = 1
        else:
            status = 0
        team = i['team']
        gamestatus.update({date:[team, status]})
    f.close()   
    f2.close() 
    return(name, gamestatus)

# Puts all player files in a dictionary, that way their existance can be checked. If the file already exists the 
# code can pull from the json file rather than from the internet (lessen the load on the website)
def filefiller(path, date):
    for file in os.listdir(f'{path}/player_jsons/{date}'):
        if file.endswith('.json'):
            file, trash = os.path.splitext(file)
            filenames.update({file: 1})

# Checks to see if the date file exists for a user specified date. If it doesn't it is created
def file_existance(path, date):
    existance = os.path.exists(f'{path}/player_jsons/{date}')
    if existance == False:
        os.mkdir(f'{path}/player_jsons/{date}')


if __name__ == '__main__':

    while date > currentyear or date < 1949:
        date = int(input("Please choose a year you would like to pull your data from: "))
    
    # connects to database 
    con = sqlite3.connect(f"BasketballPlayers.db")

    sqlfiller.tableexistance(con, date)

    file_existance(path, date)
    filefiller(path, date)
    
    if (f'playerdict_{date}.json') not in os.listdir(f'{path}/player_jsons/{date}'):
        internetgrabber.players_of_year(path, date)

    file = open(f'{path}/player_jsons/{date}/playerdict_{date}.json', 'r')
    playerfile = json.load(file)

    for player in playerfile:
        nameteamgamestatus = playerstatistics(player, date)
        name = nameteamgamestatus[0]
        
        gamestatus = nameteamgamestatus[1]
        for ineedteam in gamestatus:
            team = gamestatus[ineedteam][0]
            value = bballdicts.teamdict[team]

            if team not in d:
                d.update({team: get_roster(value, date)})

            if (d[team]['PLAYER'] == name).any() == False:
                continue
            else:
                break

        indexvalue = {name: int(d[team].loc[d[team]['PLAYER'] == name].index.values)}
        weight = (d[team]['WEIGHT'].loc[d[team].index[indexvalue[name]]])
        height = (d[team]['HEIGHT'].loc[d[team].index[indexvalue[name]]])
        heightcalc = height.split('-')
        height = int(heightcalc[0]) * 12 + int(heightcalc[1])
        heightcalc.clear()
        for gamedate in gamestatus:
            name = name.replace(' ', '_')
            team = gamestatus[gamedate][0].replace(' ', '_')
            status = gamestatus[gamedate][1]           
            data = (name, team, weight, height, gamedate, status)
            print(data, end = '\n' * 2)
            sqlfiller.tablefiller(con, data, date)
        time.sleep(10)   
    
    con.close()