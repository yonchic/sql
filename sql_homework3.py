import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory WHERE Make='Ford'")

    rows = c.fetchall()
    for r in rows:
        print("Make: {}, Model: {}, Quantity: {}".format(r[0], r[1], r[2]))