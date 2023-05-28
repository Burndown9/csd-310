"""
movies_update_and_delete.py
Jacob Hayes
2023 May 28

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

#create a function that can display results easily
def DisplayResults(cursor, title):
    #grab Name, Director, Genre, Studio
    cursor.execute("SELECT film_name as Name, "
                   "film_director as Director, "
                   "genre_name as Genre, "
                   "studio_name as 'Studio Name' "
                   "from "
                   #we need to join our tables together
                   #in order to get all of the fields
                   "film INNER JOIN genre "
                   "ON film.genre_id=genre.genre_id "
                   "INNER JOIN studio "
                   "ON film.studio_id=studio.studio_id;")
    records = cursor.fetchall()

    #make it pretty
    print("\n -- {} --".format(title))

    #iterate through results
    for film in records:
        print("Film Name: {}\n"
              "Director: {}\n"
              "Genre Name: {}\n"
              "Studio Name: {}\n".format(film[0],
                                         film[1],
                                         film[2],
                                         film[3]))

#connect using our user
try:
    db = mysql.connector.connect(**config)

    #print the successful connection, using the dictionary to fill in the blanks
    print("\n Database user {} connected to MySQL on host "
          "{} with database {}".format(config["user"],config["host"], config["database"]))

    #ready a cursor to collect records for us
    cursor = db.cursor()

    #show all of the films in the database
    DisplayResults(cursor, "DISPLAYING FILMS")

    #new film!
    cursor.execute("INSERT INTO film (film_id, "
                   "film_name, film_releaseDate, "
                   "film_runtime, film_director, "
                   "studio_id, genre_id) VALUES ("
                   "4, 'The Martian', '2015', 144, "
                   "'Ridley Scott', 1, 2);")
    
    #show that we've got the new movie
    DisplayResults(cursor, "DISPLAYING FILMS AFTER INSERT")

    #update Alien's genre to horror
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2;")
    
    #show the update
    DisplayResults(cursor, "DISPLAYING FILMS AFTER UPDATE - UPD ALIEN")

    #delete Gladiator
    cursor.execute("DELETE FROM film WHERE film_id = 1;")

    #show the update
    DisplayResults(cursor, "DISPLAYING FILMS AFTER UPDATE - DEL GLADIATOR")

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