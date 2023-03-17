from bs4 import BeautifulSoup
import requests
import json

# Grabs a list of every player's name and their player code, then puts them into a json file for access
def players_of_year(path, date):
    url = f'https://www.basketball-reference.com/leagues/NBA_{date}_totals.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(attrs = {"data-stat": "player"})
    namelist = {}


    for result in results:
        name = result.get('csk')
        tag = result.get('data-append-csv')
        if type(name) is not str:
            continue
    
        li = list(name.split(','))
        li.append(" ")
        li[2] = li[0]
        li[0] = li[1]
        li[1] = " "
        name = ''.join(li)
        li.clear()

        if tag in namelist:
            pass
        else:
            namelist.update({tag:name})


    with open(f'{path}\\player_jsons\\{date}\\playerdict_{date}.json', 'w') as data:
        data.write(json.dumps(namelist))

    data.close()






"""playername = []

f = open("playernames.txt", "r")
f2 = open("cleannames.txt", "w")
for line in f:
    if line in playername:
        pass
    else:
        playername.append(line)
        f2.write(line)
        
f.close()
f2.close()"""

"""f = open("cleannames.txt", "r")
for line in f:
    playername = line

    #url = f'https://www.basketball-reference.com{playername}'"""
