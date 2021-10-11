import sqlite3
import urllib.request, urllib.parse, urllib.error

conn = sqlite3.connect('emailexercise.sqllite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (Email TEXT, count INTEGER)')

fh = open('C:\\Users\Gaurav Shubham\Desktop\gaurav.txt', 'r')
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email,count) VALUES (?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 1000'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    print('Done')
