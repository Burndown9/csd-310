

# Bacchus Winery Database Display

import mysql.connector
from mysql.connector import errorcode

# replace 'user', 'password', 'localhost', 'database' with your MySQL credentials
#cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='database')
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='bacchus')

cursor = cnx.cursor()

# create tables
tables = {'GRAPE', 'WINE', 'SUPPLIER', 'SUPPLIES', 'INVENTORY', 'DISTRIBUTOR', 'WINE_ORDER', 'EMPLOYEE'}

def pp(cursor, data=None, rowlens=0):
    d = cursor.description
    if not d:
        return "#### NO RESULTS ###"
    names = []
    lengths = []
    rules = []
    if not data:
        data = cursor.fetchall(  )
    for dd in d:    # iterate over description
        l = dd[1]
        if not l:
            l = 12            
        l = max(l, len(dd[0])) # Handle long names
        names.append(dd[0])
        lengths.append(l)
    for col in range(len(lengths)):
        if rowlens:
            rls = [len(str(row[col])) for row in data if row[col]]
            lengths[col] = max([lengths[col]]+rls)
        rules.append("-"*lengths[col])
    format = " ".join(["%%-%ss" % l for l in lengths])
    result = [format % tuple(names)]
    result.append(format % tuple(rules))
    for row in data:
        result.append(format % row)
    return "\n".join(result)

for table_name in tables:
    sql = "SELECT * FROM " + table_name + ";"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(pp(cursor, results))
    print("\n\n\n")





cursor.close()
cnx.close()
