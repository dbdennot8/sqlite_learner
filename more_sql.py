#!usr/bin/python
# *-* coding: utf-8 *-*

import sqlite3 as lite

con = lite.connect('my_music.db')

with con:
    cur = con.cursor()

    # If Table exists, DROP deletes it, allowing the CREATE fn to 
    # set up a new table with that name.
    cur.execute("DROP TABLE IF EXISTS Favorites")
    cur.execute("CREATE TABLE Favorites(Artist TEXT, Song TEXT)")

    cur.execute("INSERT INTO Favorites (Artist, Song) VALUES(?, ?)", ('Trip Lee ', 'Longer'))
    # alternative shorter input sequence ... 
    cur.execute("INSERT INTO Favorites VALUES('Lecrae   ', 'River Jordan')")
    cur.execute("INSERT INTO Favorites VALUES('Prop     ', 'Made Straight')")
    cur.execute("INSERT INTO Favorites VALUES('Lauren D.', 'First')")
    cur.execute("INSERT INTO Favorites VALUES('KB       ', 'Open Letter')")
    cur.execute("INSERT INTO Favorites VALUES('Lecrae   ', 'Broken')")
    con.commit()
  
    def printer():
        '''Function outputs in a decent format the contents of the db'''
        cur.execute("SELECT * FROM Favorites") # generates info ordered as inserted
        # cur.execute("SELECT * FROM Favorites ORDER BY Artist") # generates output ordered alphabetically by Artist name

        rows = cur.fetchall()
        print("--"*30)
        print(" "*2 + "Rank" + " "*15 +"Artist" +" "*23 + "Song")
        print("--"*30)
        count = 1
        for row in rows:
            if row[1] != "Trip Lee":
                print()
                print((" "*3 + "{}." + " "*15 + "{}" + " "*21 + "{}").format(count, row[0], row[1]))
                count += 1
                print()
        print()
        print("--"*30)


    print()
    print("As Inserted: ")
    printer()

    cur.execute("UPDATE Favorites SET Artist = 'Denno T8 ' WHERE Song = 'Broken'")
    cur.execute("UPDATE Favorites SET Song = 'A Billion Years' WHERE Artist = 'Trip Lee '")
    print()
    print("After Update: ")
    printer()
