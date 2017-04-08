'''
Interact between Teradata and Python using the package giraffez
'''

import giraffez as gr
import pandas as pd
from pandas import DataFrame
import os

#basic operation
with gr.Cmd() as cmd:
    result = cmd.execute('select top 5 * from database.table_name')
print result

#exporting large amount of rows from Teradata table and generate a dataframe
with gr.Export(encoding='dict') as export:
    export.query = "select * from database.table_name"
    df = pd.DataFrame(export.results())
df.head()

#loading large amount of data from file to Teradata table
#You will have to create an empty Teradata table whose column name/type matches with those in the data file...
with gr.MLoad("database.table_name1") as mload:
    exit_code = mload.from_file("input.txt")
with gr.MLoad("database.table_name2") as mload:
    exit_code = mload.from_file("data.csv")

#alternatively, inserting data from file/dataframe row by row to Teradata table
#e.g.
sqlcreate = '''
create table database.EID_giraffez_gamingtable1
(
acct_id integer,
name varchar(100),
rev_bkt integer
) primary index (acct_id);
'''

with gr.Cmd() as cmd:
  result = cmd.execute(sqlcreate)

print result

with gr.MLoad("database.EID_giraffez_gamingtable1") as mload:
    rows = [(1, "A", 5), (2, "B", 6)]
    for row in rows:
        mload.load_row(row)
    exit_code = mload.finish()
    print("finished load with code {0}".format(exit_code))
    if exit_code == 0:
        mload.cleanup()

#To see the output table
with gr.Cmd() as cmd:                                  
    result2 = cmd.execute('select * from database.EID_giraffez_gamingtable1')

print result2
