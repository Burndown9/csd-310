

# Bacchus Winery Database Creation

import mysql.connector
from mysql.connector import errorcode

# replace 'user', 'password', 'localhost', 'database' with your MySQL credentials
#cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='database')
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='bacchus')

cursor = cnx.cursor()


# create tables
tables = {}

tables['GRAPE'] = (
    "CREATE TABLE GRAPE ("
    "  grape_id INT AUTO_INCREMENT,"
    "  grape_type VARCHAR(20),"
    "  grape_harvested_date DATE,"
    "  PRIMARY KEY (grape_id)"
    ") ENGINE=InnoDB")

tables['WINE'] = (
    "CREATE TABLE WINE ("
    "  wine_id INT AUTO_INCREMENT,"
    "  wine_type VARCHAR(20),"
    "  grape_id INT,"
    "  wine_bottled_date DATE,"
    "  PRIMARY KEY (wine_id),"
    "  FOREIGN KEY (grape_id) REFERENCES GRAPE(grape_id)"
    ") ENGINE=InnoDB")

tables['SUPPLIER'] = (
    "CREATE TABLE SUPPLIER ("
    "  supplier_id INT AUTO_INCREMENT,"
    "  supplier_name VARCHAR(50),"
    "  supplier_phone VARCHAR(15),"
    "  PRIMARY KEY (supplier_id)"
    ") ENGINE=InnoDB")

tables['SUPPLIES'] = (
    "CREATE TABLE SUPPLIES ("
    "  supply_id INT AUTO_INCREMENT,"
    "  supply_type VARCHAR(20),"
    "  supply_quantity INT,"
    "  supplier_id INT,"
    "  expected_delivery_date DATE,"
    "  actual_delivery_date DATE,"
    "  PRIMARY KEY (supply_id),"
    "  FOREIGN KEY (supplier_id) REFERENCES SUPPLIER(supplier_id)"
    ") ENGINE=InnoDB")

tables['INVENTORY'] = (
    "CREATE TABLE INVENTORY ("
    "  supply_id INT,"
    "  supply_quantity INT,"
    "  expected_delivery_date DATE,"
    "  actual_delivery_date DATE,"
    "  FOREIGN KEY (supply_id) REFERENCES SUPPLIES(supply_id)"
    ") ENGINE=InnoDB")

tables['DISTRIBUTOR'] = (
    "CREATE TABLE DISTRIBUTOR ("
    "  distributor_id INT AUTO_INCREMENT,"
    "  distributor_name VARCHAR(50),"
    "  distributor_phone VARCHAR(15),"
    "  PRIMARY KEY (distributor_id)"
    ") ENGINE=InnoDB")

tables['WINE_ORDER'] = (
    "CREATE TABLE WINE_ORDER ("
    "  order_id INT AUTO_INCREMENT,"
    "  distributor_id INT,"
    "  wine_id INT,"
    "  wine_bottled_date DATE,"
    "  order_date DATE,"
    "  expected_delivery_date DATE,"
    "  actual_delivery_date DATE,"
    "  quantity_sold INT,"
    "  PRIMARY KEY (order_id),"
    "  FOREIGN KEY (distributor_id) REFERENCES DISTRIBUTOR(distributor_id),"
    "  FOREIGN KEY (wine_id) REFERENCES WINE(wine_id)"
    ") ENGINE=InnoDB")

tables['SHIPMENT'] = (
    "CREATE TABLE SHIPMENT ("
    "  shipment_id INT AUTO_INCREMENT,"
    "  order_id INT,"
    "  PRIMARY KEY (shipment_id),"
    "  FOREIGN KEY (order_id) REFERENCES WINE_ORDER(order_id)"
    ") ENGINE=InnoDB")

tables['EMPLOYEE'] = (
    "CREATE TABLE EMPLOYEE ("
    "  employee_id INT AUTO_INCREMENT,"
    "  employee_name VARCHAR(50),"
    "  employee_role VARCHAR(20),"
    "  PRIMARY KEY (employee_id)"
    ") ENGINE=InnoDB")

tables['PAYROLL'] = (
    "CREATE TABLE PAYROLL ("
    "  employee_id INT,"
    "  hours_worked INT,"
    "  month_year DATE,"
    "  FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id)"
    ") ENGINE=InnoDB")

tables['MARKETING'] = (
    "CREATE TABLE MARKETING ("
    "  campaign_id INT AUTO_INCREMENT,"
    "  wine_type VARCHAR(20),"
    "  campaign_cost INT,"
    "  PRIMARY KEY (campaign_id)"
    ") ENGINE=InnoDB")

tables['PRODUCTION'] = (
    "CREATE TABLE PRODUCTION ("
    "  production_id INT AUTO_INCREMENT,"
    "  wine_id INT,"
    "  PRIMARY KEY (production_id),"
    "  FOREIGN KEY (wine_id) REFERENCES WINE(wine_id)"
    ") ENGINE=InnoDB")

for table_name in tables:
    table_description = tables[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
