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
        namecheck = result.get('csk')
        if type(namecheck) is not str:
            continue
        name = (result.find('a').contents[0])
        tag = result.get('data-append-csv')

        if tag in namelist:
            pass
        else:
            namelist.update({tag:name})


    with open(f'{path}/player_jsons/{date}/playerdict_{date}.json', 'w') as data:
        data.write(json.dumps(namelist))

    data.close()