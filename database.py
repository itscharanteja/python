import sqlite3
conn = sqlite3.connect("test.db")
if conn:
    print("Connected successfully")

else:
    print(conn)
