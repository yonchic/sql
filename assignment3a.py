import sqlite3
import random



with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    random_num = [(random.randint(0, 100),) for i in range(100)]

    c.execute("CREATE TABLE random_integers (numbers INT)")
    c.executemany("INSERT INTO random_integers VALUES(?)", random_num)

