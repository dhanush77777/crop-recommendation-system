import sqlite3

con = sqlite3.connect('test.db',isolation_level=None)
cur = con.cursor()
cur.execute("SELECT * FROM FOOBAR")
data = cur.fetchall()
print(data)