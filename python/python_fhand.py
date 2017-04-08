fhand = open('/path/file.txt')
list_element = []
for line in fhand:
    line = line.rstrip()
    word = line.split()
    element = word[0]
    list_element.append(element)

'''
e.g. check the column type in a dataframe read from Teradata
'''

import pyodbc
import pandas as pd

fhand = open('/path/variable_to_keep.txt')
list_var = []
for line in fhand:
    line = line.rstrip()
    word = line.split(',')
    var = word[0]
    list_var.append(var)


conn = pyodbc.connect('DRIVER={Teradata};DBCNAME=oneview;UID=abc123;PWD=ABCDEF00;', autocommit = True ) 
sqlcreate = '''
select top 50* from ud206.lzq857_table
'''
df1 = pd.read_sql(sqlselect, conn)
for y in df1.columns:
    if(df1[y].dtype = object and y in list_var):
        print y
