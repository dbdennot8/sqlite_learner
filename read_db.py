import sqlite3 as lite
import sys

con = lite.connect('presidential.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT Aspirants.name, VotesFor.VotesFor FROM VotesFor INNER JOIN Aspirants ON Aspirants.ID = VotesFor.Uid")

    rows = sorted(cur.fetchall())
    sum_all = 0
    percent = 0
    print()
    for row in rows:
        sum_all += row[1]
    
    print("--"*30)

    for row in rows:      
        print(("{}:     " + "{}" + "     {} %").format(row[0], row[1], (100*row[1]/sum_all)))
        percent += (100*row[1]/sum_all)
    
    print("--"*30)
    print(("Total Votes Cast:" +" "*5 + "{}" +"     {} %").format(sum_all, percent))
    print("--"*30)
    print()
