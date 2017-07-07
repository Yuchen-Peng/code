'''
In itunes, go files -> library -> export library, one can export the itune library as a XML format file.
XML has a “dictionary over dictionary over dictionary” structure. 
Use package xml.etree.ElementTree to get the entry from the XML file.
'''

import xml.etree.ElementTree as ET
import sqlite3

fname = '.\Library.xml'
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
# this find all entries at the third level of dictionary, each entry like ‘<format>entry value</format>’
# e.g. <key>Artist</key>, <string>Queen</string>
# We can loop through the entries in all to read in data, e.g.
def lookup(entry, column):
  found = False
  for child_entry in entry:
    if found: return child_entry.text
    if child_entry.tag == 'key' and child_entry.text == column:
      found = True
  return None
  
'''
Create the tables in the logic picture, include the foreign keys in the table (if there is):
'''

cur.executescript('''
  CREATE TABLE IF NOT EXISTS Artist(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
  );

  CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
  );

  CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
  );

  CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER, genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
  );
''')

'''
Loop through the XML file and insert into table the values:
'''

for entry in all:
  if ( lookup(entry, 'Track ID') is None ): continue
  
  name = lookup(entry, 'Name')
  genre = lookup(entry, 'Genre')
  artist = lookup(entry, 'Artist')
  album = lookup(entry, 'Album')
  count = lookup(entry, 'Play Count')
  rating = lookup(entry, 'Rating')
  length = lookup(entry, 'Total Time')

  if name is None or artist is None or album is None:
    continue

  print name, artist, album, count, rating, length

  cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
  cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

  cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
  cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

  cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
  cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

  cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count, genre_id ) )

  conn.commit()

