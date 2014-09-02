import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory")

    res = c.fetchall()

    for xmake, xmodel, xquantity in res:
        print("Make: {}, Model: {}\nQuantity: {}".format(xmake, xmodel, xquantity))
        c.execute("SELECT COUNT(model) FROM orders WHERE model = '{}'".format(xmodel))
        l = c.fetchall()
        print("Order Count: {}\n".format(l[0][0]))      



