#python to teradata and redshift

import pyodbc 
import psycopg2  
import pandas as pd 
from pandas import DataFrame
import getpass

#for teradata

user = getpass.getuser()
pwd = getpass.getpass()

conn = pyodbc.connect('DRIVER={Teradata};DBCNAME=oneview;UID=' +user + ';PWD=' + pwd+';',autocommit=True)

#conn = pyodbc.connect('DRIVER={Teradata};DBCNAME=oneview;UID=abc123;PWD=ABCDEF00;', autocommit = True )  #hard-code

#for redshift
user = 'EID'
pwd = getpass.getpass()
conn_redshift=psycopg2.connect(dbname= 'db', host='pbcdwp.cloud.capitalone.com', port= 5439, user= user, password= pwd)

cursor = conn.cursor()

sqlq = '''
SQL code
'''

cursor.execute(sqlq)

#read cursor result to a dataframe
df = DataFrame(cursor.fetchall())
df.columns = cursor.keys()

#sample script for creating a table, read to dataframe, and output to csv
sqlcreate = '''
create multiset table UD206.EID_gaming_table
as
(select
a.Acct_ID,
case
    when a.strategy_segment like '%CIA%' then 'Internet'
    when a.strategy_segment like '%DM%' then 'Direct_Mail' 
    when a.strategy_segment like '%Bank%' then 'Bank'
    else 'error'
end as channel,
case 
    when a.SB_Revenue <=100000  then 1
    when a.SB_Revenue <=250000  then 2
    when a.SB_Revenue <=500000  then 3
    when a.SB_Revenue <=1000000  then 4
    when a.SB_Revenue>1000000  then 5
    else 99 
end as rev_bkt
from UD442.ONEM_CCA_MODEL_INPUT_VW a
where strategy_segment in ('Small Business CIA 2x', 'Small Business CIA 1pt5x','Small Business CIA - Access','Small Business CIA - Revolver', 'SB DM 1pt5x CASH ITA', 'SB DM 2x CASH FEE ITA', 'SB Bank', 'SB DM 1x CASH ITA', 'SB DM 2x CASH NO FEE ITA')
and open_dt between '2014-01-01' and '2016-12-31'
and acct_id is not null)
with data
primary index (acct_id)
'''

sqlselect = '''
select * from UD206.lzq857_gaming_table;
'''

df1 = pd.read_sql(sqlcreate, conn)
df1.to_csv('~/prod/user/sam/us/card/cca/vr/non_npi/lzq857/.../table_name.csv')


# alternative approach to write to CSV... 
import csv 

out_file = '/prod/user/sam/us/card/cca/vr/non_npi/lzq857/.../table_name.csv' 

with open(out_file, 'w') as f: csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL) 
csv_writer.writerow([i[0] for i in cursor.description]) 
# write headers 
csv_writer.writerows(cursor)


