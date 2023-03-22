import sqlite3

#creates a table if a table for that year doesn't currently exist
def tableexistance(con, date):
    # creates a cursor to move around the database with
    cur = con.cursor()
    cur.execute(f'CREATE TABLE IF NOT EXISTS Year_{date} (Name TEXT, Team TEXT, Weight INT, Height INT, GameDate DATE, Status BIT)')

#fills table with data. Will pull game dates to make sure no overlapping entries are entered
def tablefiller(con, data, date):
    # creates a cursor to move around the database with
    cur = con.cursor()
    repeat = cur.execute(f'SELECT Name, GameDate FROM Year_{date} WHERE EXISTS(SELECT Name, GameDate FROM Year_{date} WHERE Name = "{data[0]}" AND GameDate = "{data[4]}")')
    if repeat == True:
        return 1
    else:
        cur.execute(f"INSERT INTO Year_{date} VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')")
        con.commit()

