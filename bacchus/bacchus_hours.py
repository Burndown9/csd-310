
#show employee hours (as a sum over the last four quarters for each employee)

import mysql.connector

# replace 'user', 'password', 'localhost', 'database' with your MySQL credentials
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='bacchus')


cursor = cnx.cursor()

# add up all the employee hours and name
## customize for date ranges by only taking records where p.month_year meets the criteria
query = """
    SELECT e.employee_id,
    e.employee_name,
    SUM(p.hours_worked) as hours
    FROM EMPLOYEE e
    JOIN PAYROLL p
    ON e.employee_id = p.employee_id
    GROUP BY employee_id;
"""


cursor.execute(query)

# Print header for the report
print(f"{'id':<6} {'Name':<18} {'Hours':<20}")
print(f"{'-'*5} {'-'*18} {'-'*20}")

#print actual data
for (employee_id, employee_name, hours) in cursor:
    print(f"{employee_id:<6} {employee_name:<18} {hours:<5} hours worked")

cursor.close()
cnx.close()
