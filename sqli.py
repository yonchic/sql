import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname FROM employees")

    # fetchall() retrieves all record from the query
    rows = c.fetchall()

    for row in rows:
        print(row[0], row[1])