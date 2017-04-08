sqlstr = 'SELECT acct_id, balance FROM Accounts ORDER BY balance DESC LIMIT 10'

#for loop
for row in cursor.execute(sqlstr) :
    print str(row[0]), row[1]

#while loop using fetchone()    
row = cursor.fetchone()
while row is not None:
    print str(row[0]), row[1]
    row = cursor.fetchone()
