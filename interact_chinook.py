'''Code to interact with a sample db I downloaded form net'''

import sqlite3 as lite

con = lite.connect('chinook.db')

with con:
    cur = con.cursor()

    def printer():
        '''Outputs stuff to screen'''
        rows = cur.fetchall()
        print()
        for row in rows:
            print()
            print(row)
        print()

    # Display contents of table 'employees'
    cur.execute('SELECT * FROM employees')
    print("Employees:")
    printer()
    
    # Display contents of table 'albums'
    cur.execute('SELECT * FROM albums WHERE AlbumId <= 5')
    print("Albums:")
    printer()

    # Display all table names and info
    # cur.execute('SELECT * FROM sqlite_master WHERE type = "index" or type = "table" ')
    # print()
    # print("Info on Tables:")
    # printer()
    # print()