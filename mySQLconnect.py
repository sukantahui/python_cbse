# https://pynative.com/python-mysql-select-query-to-fetch-data/
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='metal_db',
                                         user='root',
                                         password='sukantahui')
    sql_select_Query = """select * from ledgers where id=%s"""
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query, (15,))
    records = cursor.fetchall()
    print("Fetching each row using column name")

    for row in records:
        id = row["id"]
        name = row["ledger_name"]
        print(id, name)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

# Adding records to ledger_groups
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='metal_db',
                                         user='root',
                                         password='sukantahui')
    mySql_insert_query = """insert into ledger_groups (id,group_name) 
                            VALUES (NULL,'test') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into ledger_groups table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
