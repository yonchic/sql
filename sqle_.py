# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8000000)")

    conn.commit()
except sqlite3.OperationalError as e:
    print("Oops! Somethng went wrong. Try again...", e)

conn.close()