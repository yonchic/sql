import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    cars = [
        ('Ford', 'Focus', 10),
        ('Ford', 'Ibiza', 40),
        ('Ford', 'Mustang', 8),
        ('Honda', 'Civic', 20),
        ('Honda', 'CRX3', 6)
    ]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)