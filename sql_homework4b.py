import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT inventory.Make,
                                   inventory.Model,
                                   inventory.Quantity,
                                   orders.order_date
                   FROM inventory, orders
                   WHERE inventory.Model = orders.model
            """)


    rows = c.fetchall()

    for r in rows:
        print("Make {}, Model {}\nQuantity {}\nOrder Date {}\n".format(r[0], r[1], r[2], r[3]))
