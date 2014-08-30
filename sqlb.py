import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 8000000)")
    c.execute("INSERT INTO population VALUES('Warsow', 'WA', 1500000)")