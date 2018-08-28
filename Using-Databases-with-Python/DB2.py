import xml.etree.ElementTree as ET
import mysql.connector as sql

conn = sql.connect(user='root',password='Dheeraj@1998',host='127.0.0.1',database='python')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Artist;")
cur.execute("DROP TABLE IF EXISTS Genre;")
cur.execute("DROP TABLE IF EXISTS Album;")
cur.execute("DROP TABLE IF EXISTS Track;")


cur.execute("CREATE TABLE Artist (id INTEGER(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30) UNIQUE);")

cur.execute('''CREATE TABLE Genre (id  INTEGER(11) NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,name VARCHAR(30) UNIQUE);''')

cur.execute('''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
    artist_id  INTEGER,
    title VARCHAR(30) UNIQUE
);''')

cur.execute('''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
    title VARCHAR(30) UNIQUE,
    album_id  INTEGER(11),
    genre_id  INTEGER(11),
    len INTEGER(11), rating INTEGER(11), count INTEGER(11)
);''')

def find_item(d, key):
	found = False
	for child in d:
		if(found): return(child.text)
		if(child.tag == 'key' and child.text == key):
			found = True

fname = 'Library.xml'

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for items in all:
	name = find_item(items, 'Name')
	genre = find_item(items,'Genre')
	artist = find_item(items, 'Artist')
	album = find_item(items, 'Album')
	count = find_item(items, 'Play Count')
	rating = find_item(items, 'Rating')
	length = find_item(items, 'Total Time')
    
	if name is None or artist is None or genre is None or album is None or count is None or rating is None or length is None: 
		continue
    
	print(name,genre,artist,album,count,rating,length)
    
	cur.execute("INSERT IGNORE INTO Artist(name) VALUES (%s);",(artist,))
	cur.execute("SELECT id FROM Artist WHERE name = %s ", (artist,))
	artist_id = cur.fetchone()[0]
    
	cur.execute("INSERT IGNORE INTO Genre(name) VALUES (%s);", ( genre, ) )
	cur.execute("SELECT id FROM Genre WHERE name = %s ", (genre, ))
	genre_id = cur.fetchone()[0]

	cur.execute("INSERT IGNORE INTO Album(artist_id,title) VALUES (%s,%s);", ( artist_id,album, ) )
	cur.execute("SELECT id FROM Album WHERE title = %s ", (album, ))
	album_id = cur.fetchone()[0]
    
	cur.execute("INSERT IGNORE INTO Track (title,album_id,genre_id,len,rating,count) VALUES ( %s, %s, %s, %s, %s, %s);", ( name, album_id, genre_id, length, rating, count, ) )
	conn.commit()

cur.close()
conn.close()
	
