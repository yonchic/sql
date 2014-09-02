# SQL Functions

import sqlite3

with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  #create a dictionary of sql queries
  sql = {'avaeage': "SELECT AVG(population) FROM population",
         'maximum': "SELECT MAX(population) FROM population",
         'minimum': "SELECT MIN(population) FROM population",
         'sum': "SELECT SUM(population) FROM population",
         'count': "SELECT COUNT(city) FROM population"}

  #run each sql query item in the dictionary
  for keys, values in sql.iteritems():
    #run sql
    c.execute(values)
    result = c.fetchall()

    #output the result to screen
    print("{}: {}".format(keys, result[0]))