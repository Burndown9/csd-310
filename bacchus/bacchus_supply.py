


import mysql.connector

# replace 'user', 'password', 'localhost', 'database' with your MySQL credentials
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='bacchus')


cursor = cnx.cursor()

query = """
    SELECT s.supplier_name, 
           MONTH(su.actual_delivery_date) AS delivery_month, 
           su.supply_type, 
           su.supply_quantity, 
           su.expected_delivery_date, 
           su.actual_delivery_date
    FROM SUPPLIES su
    JOIN SUPPLIER s
    ON su.supplier_id = s.supplier_id
"""

cursor.execute(query)

report = {}
for (supplier_name, delivery_month, supply_type, supply_quantity, expected_delivery_date, actual_delivery_date) in cursor:
    delay = (actual_delivery_date - expected_delivery_date).days
    key = (supplier_name, delivery_month)
    if key in report:
        report[key].append(delay)
    else:
        report[key] = [delay]


# Print header for the report
print(f"{'Supplier':<26} {'Month':<8} {'Average Delay':<5}")
print(f"{'-'*25} {'-'*8} {'-'*15}")

# Display results
for (supplier, month), delays in report.items():
    avg_delay = sum(delays) / len(delays)
    print(f"{supplier:<26} {month:<8} {avg_delay:<5.2f} days")

cursor.close()
cnx.close()
