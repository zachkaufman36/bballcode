# bballcode
A project designed around finding the average change in weight for an NBA team over an entire season. This will be displayed by fun graphics. Used as a learning tool to learn MySQL, Ubuntu, web scraping, matplotlib, ect. 

FIRST STAGE:
Pick a website to gather data from. Basketball Reference was chosen and 2 APIs were found. One was used to gather game-to-game data while the other is used to gather players' weight and heights. 
Challenges:
1. Getting the original API to work on my system. Ended up learning about WSL2, Ubuntu, and virtual environments
2. Setting up code to be as system independant as possible. I was switching between working on two different computers, so I wanted this to be very easy to move around. I used this opportunity to refamiliarize myself with Github. The code creates
   all files and subdirectories it needs into the directory it's being run from.
3. The original way I was going to do it was I was going to scrape a player's individual page for their full name. This quickly became too many requests for the website and they blocked me. I worked around this by pulling from a page that had a full
   list of players for a season.
4. I set up the code to try and pull as infrequently from the website as possible. It pulls a player's information once, then stores that info in a JSON file. It continuously refers to the players JSON file until it is empty, then it moves to the next
   player. I also have it do this with team info, except that is saved into a dictionary.

SECOND STAGE:
Upload all data into a MySQL database. The code will create tables based on the year entered.
Challenges:
1. I have never used SQL before this. I had to learn basic SQL commands, table layout, column typings, and which version of SQL I wanted to use. I settled on MySQL based on the recommendation of a friend, plus it's easy integration with Python.
2. The second API was used because the first one couldn't pull a player's weight, and scraping individual pages was too much strain on the website. This API would display info in a pandas dataframe that I then pulled specific values from by 
   programmatically identifying the index a player had in a dataframe.
3. Players being traded was initially an issue. A player might exist on one team through technicality, but the team dataframe wouldn't show them. This was gotten around by checking to see if the player existed on the team, and if they didn't it
   would check the next team in the player's JSON file.
4. Even with all the precautions laid out the strain on the website was too high. I ended up installing a 10 second sleep command in between players to spread out the pull requests. This was the shortest multiple of 5 window that I could find
5. Originally I was going to have it read through the table in the database and make sure it wasn't adding double entries, but that was going to become a logistical problem so fast that it was faster to delete the whole thing and refill it. 
   Maybe now that it's fully working I'll reinstall a check for the database, so it doesn't fill the same one twice

THIRD STAGE:
Data analysis. This will include creating graphics, finding the solution, and manipulating the data gathered to find other data points.
Challenges:
1. The biggest challenge was finding a way to display the data. Originally I wanted to do a line plot, but then I thought of racing bar graphs and tried that. However the data moved too quickly and it made that form of display very unpleasant to
   look at. I tried the line plot as well, but there are too many points of data so I decided to go with the delta from the beginning and end of the season, and make it into bar graphs.
2. Originally I was going to do a double dictionary to hold all the data, but I found quickly that the second dictionary wouldn't always switch when I wanted it to. I got around this by making a Team object, then calling the object whenever I wanted
   to access that team's dictionary.
3. I never got show() to work. I'm not sure why I can't get it to work, I tried messing with the backend but that did nothing. Saving the graph instead did the job.

THINGS I'D DO DIFFERENT:
1. I would narrow down the data points. Whether it be team specific, or have it be game by game, but the all at once approach for data this volatile never worked.
2. Next time I'd like to pick something that can have an actual conclusion drawn from it. This is a fun data manipulation exercise, but there isn't anything to be learned from it. I have height, so I could figure out the best BMI to be with this data
3. Better commenting. I know everything that's going one so I didn't bother commenting much, but looking back on it I'd have a hard time knowing why I made certain decisions.
4. More of a next step would be turning this into a website. Having it be interactable could be very valuable.
5. Add in teams from the past. Currently it breaks if it tries to reference a nonexisting team.