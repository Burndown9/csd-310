"""
mysql_test.py
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

    input("\n\n     Press any key to continue...")

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