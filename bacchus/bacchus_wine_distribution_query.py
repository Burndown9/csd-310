import mysql.connector
from mysql.connector import errorcode
import credentials

try:
    db = mysql.connector.connect(**credentials.config)
    
    print("\n Database User {} connected to MySQL on host {} with database {}".format(credentials.config["user"], credentials.config["host"], credentials.config["database"]))

    input("\n\n Press enter to continue...")

    cursor = db.cursor()

    query = """
        Select 
            w.wine_type,
            wo.quantity_sold,
            d.distributor_name
        FROM
            wine_order AS wo
        JOIN
            distributor AS d 
        ON 
            d.distributor_id = wo.distributor_id
        JOIN
            wine AS w
        ON
            w.wine_id = wo.wine_id
"""
    cursor.execute(query)

    query_results = cursor.fetchall()

    print("\n -- DISPLAYING QUERY RESULTS --\n\n")

    max_width = max(max(len(str(col)) for col in row) for row in query_results)
    HeaderNames = ["Wine Type", "Sales", "Distributor"]

    formatted_header = [str(i).ljust(max_width) for i in HeaderNames]
    print(" | ".join(formatted_header)+"\n--------------------------------------------------")

    for row in query_results:

        formatted_row = [str(col).ljust(max_width) for col in row]
        print(" | ".join(formatted_row))



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The specified username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("\n MySQL connection closed.")