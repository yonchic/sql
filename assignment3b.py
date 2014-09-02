import sqlite3


with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    sql = {'1': "SELECT AVG(numbers) FROM random_integers",
           '2': "SELECT MAX(numbers) FROM random_integers",
           '3': "SELECT MIN(numbers) FROM random_integers",
           '4': "SELECT SUM(numbers) FROM random_integers"}

    while True:
        print("Would you like to perform an aggregation:")
        print("(1) AVG")
        print("(2) MAX")
        print("(3) MIN")
        print("(4) SUM")
        print("or would you like exit: (0)")
    
    
        input_from_user = str(input())
    
        if input_from_user in ['1', '2', '3', '4']:

            c.execute(sql[input_from_user])
            res = c.fetchall()

            print("The result is: {}\n".format(res[0][0]))

        elif input_from_user == '0':
            break
        else:
            print("I do not understand your comment, please try again.\n")

    print("Thank You :)")


