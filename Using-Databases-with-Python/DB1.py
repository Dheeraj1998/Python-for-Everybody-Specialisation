import mysql.connector as sql
import re

conn = sql.connect(user='root',password='Dheeraj@1998',host='127.0.0.1',database='python')
cur = conn.cursor()

if conn.is_connected():
	print("Success!")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER);")

fname = 'mbox.txt'
fh = open(fname)

emails = []
total_number = {}

for line in fh:
	if line.startswith('From:'):
		email = re.findall('@.*',line)[0][1:]
		emails.append(email)

for x in emails:
	if x not in total_number:
		total_number[x] = 1
	else:
		total_number[x] = total_number[x] + 1
		
for domain in total_number:
	cur.execute("INSERT INTO Counts VALUES('" + domain + "'," + str(total_number[domain]) + ");")

conn.commit()
print("Data added successfully!")

cur.close()
conn.close()
