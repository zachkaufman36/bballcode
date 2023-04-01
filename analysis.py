import sqlite3
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


teams = {} # Data in this dictionary will be {team: Teams}
fullinfo = {}
team_colors = {"MIAMI_HEAT": "#98002e", "MILWAUKEE_BUCKS": "#00471b", "NEW_ORLEANS_PELICANS": "#001641", "SAN_ANTONIO_SPURS": "#c4ced3", "BROOKLYN_NETS": "#000000", "PHOENIX_SUNS": "#1d1160", "MEMPHIS_GRIZZLIES": "#5d76a9", 
               "CLEVELAND_CAVALIERS": "#860038", "ORLANDO_MAGIC": "#007dc5", "CHICAGO_BULLS": "#ce1141", "LOS_ANGELES_LAKERS": "#552582", "PORTLAND_TRAIL_BLAZERS": "#e03a3e", "TORONTO_RAPTORS": "#ce1141", "OKLAHOMA_CITY_THUNDER": "#007dc3", 
               "HOUSTON_ROCKETS": "#ce1141", "WASHINGTON_WIZARDS": "#002b5c", "UTAH_JAZZ": "#00471b", "SACRAMENTO_KINGS": "#5b2b82", "CHARLOTTE_HORNETS": "#00788c", "NEW_YORK_KNICKS": "#f58426", "DENVER_NUGGETS": "#ffc627", 
               "LOS_ANGELES_CLIPPERS": "#c8102e", "GOLDEN_STATE_WARRIORS": "#ffc72c", "MINNESOTA_TIMBERWOLVES": "#78be20", "DETROIT_PISTONS": "#c8102e", "DALLAS_MAVERICKS": "#c8102e", "INDIANA_PACERS": "#002d62", "ATLANTA_HAWKS": "#c4d600", 
               "PHILADELPHIA_76ERS": "#006bb6", "BOSTON_CELTICS": "#007a33"}
graph_colors = []

class Team:
    
    def __init__(self):
        self.games = {} # will have {GameDate: Total Weight}

    def game_filler(self, GameDate):
        if GameDate not in self.games:
            self.games.update({GameDate: 0})

    def weight_filler(self, GameDate, weight):
        self.games[GameDate] += weight
    
    def start_weight(self):
        gamekeys = list(self.games.keys())
        gamekeys.sort()
        return self.games[gamekeys[0]], gamekeys
    
    def change_weight(self):
        startweight, gamekeys = self.start_weight()
        return startweight - self.games[gamekeys[-1]] 
          
    def data_filler(self):
        avg_weight = 0
        startweight, gamekeys = self.start_weight()
        for key in gamekeys:
            self.games[key] -= startweight
            avg_weight += self.games[key]
        avg_weight = avg_weight/len(list(gamekeys))
        return avg_weight
    
    def graph_values(self):
        return {'dates': self.games.keys(), 'weights': self.games.values()}

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def sql_data(con, date): #input data into dataframe that can be used for bargraph race
    
    cur = con.cursor()
    data = cur.execute(f'SELECT Team, Weight, GameDate, Status FROM Year_{date}')

    for d in data:
        teamname, playerweight, GameDate, status = d[0], d[1], d[2], d[3]
        
        if teamname not in teams:
            teams.update({teamname: Team()})
        
        teams[teamname].game_filler(GameDate)
        
        if status == 1: 
            teams[teamname].weight_filler(GameDate, playerweight)
        
        if d[3] == 0:
            pass
    
    keylist = list(teams.keys())

    """for key in keylist:
        fullinfo.update({key: teams[key].data_filler()})
    df = pd.DataFrame(data = fullinfo)
    print(df)
    for key in keylist:
        d = teams[key].graph_values()
        plt.plot('dates', 'weights', 'r-', data=d, marker = 'o', markerfacecolor = 'blue', label = key)
        plt.legend()
        plt.savefig(f'2021_{key}_testergraph.png')# figure out how to make this displayable"""
        
    #colors = [(152, 0, 46),(0, 71, 27),(0, 22, 65),(196, 206, 211),(0, 0, 0),(29, 17, 96),(93, 118, 169),(134, 0, 56),(0, 125, 197),(206, 17, 65),(85, 37, 130),(224, 58, 62),(206, 17, 65),(0, 125, 195),(206, 17, 65),(0, 43, 92),(0, 71, 27),(91, 43, 130),(0, 120, 140),(245, 132, 38),(255, 198, 39),(200, 16, 46),(255, 199, 44),(120, 190, 32),(200, 16, 46),(200, 16, 46),(0, 45, 98),(196, 214, 0),(0, 107, 182),(0, 122, 51)]
    #x = 0
    for key in keylist:
        fullinfo.update({key: teams[key].data_filler()})
        graph_colors.append(team_colors[key])
        """f = open('writekeys.txt','a')
        f.write(f' "{key}": "{rgb2hex(colors[x][0],colors[x][1],colors[x][2])}",')
        x += 1
    f.close()"""

    values = list(fullinfo.values())
    figure(figsize=(18, 18), dpi=100)
    plt.bar(keylist, values,color = graph_colors)
    plt.xticks(rotation=45, ha='right')
    plt.title('NBA WeightWatchers Award')
    plt.xlabel('Teams')
    plt.ylabel('Beginning Vs End of Season Weight')
    
    plt.savefig(f'{date}_testergraph.png')
    


if __name__ == '__main__':

    con = sqlite3.connect(f"BasketballPlayers.db")
    sql_data(con, 2021)
    