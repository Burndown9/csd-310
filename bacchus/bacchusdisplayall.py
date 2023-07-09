

import mysql.connector
from mysql.connector import errorcode

# replace 'user', 'password', 'localhost', 'database' with your MySQL credentials
#cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='database')
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='bacchus')

cursor = cnx.cursor()

# create tables
tables = ['GRAPE', 'WINE', 'SUPPLIER', 'SUPPLIES', 'INVENTORY', 'DISTRIBUTOR', 'WINE_ORDER', 'SHIPMENT', 'EMPLOYEE']

for table_name in tables:
    print(f"\n---{table_name}---\n") # print table name

    # get column names
    cursor.execute(f"SHOW COLUMNS FROM {table_name};")
    columns = cursor.fetchall()
    col_names = [column[0] for column in columns]
    print(', '.join(col_names)) # print column names

    # get and print rows
    cursor.execute(f"SELECT * FROM {table_name};")
    for row in cursor:
        print(row)

cursor.close()
cnx.close()
