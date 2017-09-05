#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite

con = lite.connect('presidential.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Aspirants")
    cur.execute("CREATE TABLE Aspirants(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Aspirants VALUES(1, 'Uhuru Kenyatta')")
    cur.execute("INSERT INTO Aspirants VALUES(2, 'Raila Odinga')")
    cur.execute("INSERT INTO Aspirants VALUES(3, 'Ekuru Aukot')")
    cur.execute("INSERT INTO Aspirants VALUES(4, 'Abduba Dida')")
    cur.execute("INSERT INTO Aspirants VALUES(5, 'Spoilt Votes')")

    cur.execute("DROP TABLE IF EXISTS VotesFor")
    cur.execute("CREATE TABLE VotesFor(Id INT, Uid INT, VotesFor INT)")
    cur.execute("INSERT INTO VotesFor VALUES(1, 1, 8400323)")
    cur.execute("INSERT INTO VotesFor VALUES(2, 2, 7000000)")
    cur.execute("INSERT INTO VotesFor VALUES(3, 3, 500000)")
    cur.execute("INSERT INTO VotesFor VALUES(4, 4, 200000)")
    cur.execute("INSERT INTO VotesFor VALUES(5, 5, 1000000)")

con.close()
