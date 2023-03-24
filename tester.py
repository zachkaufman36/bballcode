from bs4 import BeautifulSoup
import requests
import json

url = f'https://www.basketball-reference.com/leagues/NBA_2021_totals.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(attrs = {"data-stat": "player"})
namelist = {}


for result in results:
    name = result.get('csk')
    tag = result.get('data-append-csv')
    if type(name) is not str:
        continue
    print(name)
    if tag == 'baglema01':
        break
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