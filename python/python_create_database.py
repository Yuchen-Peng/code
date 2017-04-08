'''
This example shows how to create a table in a database and 
to insert data from reading other files to the table, by 
creating a table that counts the number of emails from each
sender organization
'''


import pyodbc
import sqlite3

path = 'file path/'
conn = sqlite3.connect(path + 'emaildb.sqlite')
cur = conn.cursor()

#Delete pre-exist table
cur.execute('''DROP TABLE IF EXISTS Counts''')

#Create empty table
cur.execute('''Create TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
#enter fname mbox.txt
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    #get the email address
    pieces = email.split('@')
    org = pieces[1]
    #get the organization from the email address
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    #this select the row in the table Counts whose org column is the one just get
    row = cur.fetchone()
    #choose the row as the output of the select statement
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
                #org is insert to the ? place
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    # Update the counts to each org
    
conn.commit()

cur.close()
