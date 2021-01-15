# https://pynative.com/python-mysql-select-query-to-fetch-data/
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='metal_db',
                                         user='root',
                                         password='sukantahui')
    sql_select_Query = "select * from ledgers"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Fetching each row using column name")

    for row in records:
        id = row["id"]
        name = row["ledger_name"]
        print(id, name)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

