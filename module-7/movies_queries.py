"""
movies_queries.py
Jacob Hayes
2023 May 24

Purpose: Connect to a SQL database and execute commands using a Python file.
"""

#import the required tools
import mysql.connector
from mysql.connector import errorcode

#configure the user that was created by a previous program's execution
config = {
    "user" : "movies_user",
    "password" : "popcorn",
    "host" : "127.0.0.1",
    "database" : "movies",
    "raise_on_warnings" : True
}

#connect using our user
try:
    db = mysql.connector.connect(**config)

    #print the successful connection, using the dictionary to fill in the blanks
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #ready a cursor to collect records for us
    cursor = db.cursor()

    #QUERY 1 - display ALL records for the studio tables
    cursor.execute("SELECT * FROM studio")
    records = cursor.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")

    for record in records:
        print("\nStudio ID: {}\nStudio Name: {}".format(record[0], record[1]))

    #QUERY 2 - display ALL records for the genre tables
    cursor.execute("SELECT * FROM genre")
    records = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")

    for record in records:
        print("\nGenre ID: {}\nGenre Name: {}".format(record[0], record[1]))

    #QUERY 3 - display movie names for movies WHERE runtime < 2 hours
    cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
    records = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")

    for record in records:
        print("\nFilm Name: {}\nRuntime: {}".format(record[1], record[3]))

    #QUERY 4 - display all (film names + directors) in order of director name
    cursor.execute("SELECT * FROM film ORDER BY film_director")
    records = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")

    for record in records:
        print("\nFilm Name: {}\nDirector: {}".format(record[1], record[4]))
    
    input("\n\n     Press Enter to continue...")

##handle errors
except mysql.connector.Error as err:
    ##ACCESS DENIED
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or password are invalid!")
    
    ##BAD DB
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     That database doesn't exist!")

    ##all other errors
    else:
        print(err)
    
finally:
    #close the db
    db.close