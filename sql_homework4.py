import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #c.execute("""CREATE TABLE orders
    #        (make TEXT, model TEXT, order_date DATE)
    #    """)

    orders = [
        ('Ford', 'Focus', '2013-12-01'),
        ('Ford', 'Focus', '2012-09-19'),
        ('Ford', 'Focus', '2011-03-23'),
        ('Ford', 'Ibiza', '2012-04-21'),
        ('Ford', 'Ibiza', '2004-02-01'),
        ('Ford', 'Ibiza', '2012-04-05'),
        ('Ford', 'Mustang', '1978-07-11'),
        ('Ford', 'Mustang', '1981-05-12'),
        ('Ford', 'Mustang', '1999-01-19'),
        ('Honda', 'CRX3', '2012-04-21'),
        ('Honda', 'CRX3', '2004-02-01'),
        ('Honda', 'CRX3', '2012-04-05'),
        ('Honda', 'Civic', '1978-07-11'),
        ('Honda', 'Civic', '1981-05-12'),
        ('Honda', 'Civic', '1999-01-19'),
    ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
