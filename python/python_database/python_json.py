'''
JSON is basically a list of lists/dicts. Use package json to read JSON by Python
'''

import json
import sqlite3

try:
  str_data = open('./data.json').read() # read the whole .json file into memory
except:
  raise Exception('Error in read in the file')
json_data = json.loads(str_data)
# now we can loop through json_data for each entry
