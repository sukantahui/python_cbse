import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


# adding book
def addBook(serial, name, author, publisher, publication):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library_db',
                                             user='root',
                                             password='sukantahui')
        cursor2 = connection.cursor()
        mySql_insert_query2 = """insert into books (
                                   id
                                  ,serial
                                  ,book_name
                                  ,author
                                  ,publisher
                                  ,publication
                                ) VALUES (
                                   NULL, %s,%s, %s, %s,%s
                                )"""

        recordTuple = (serial, name, author, publisher, publication)
        cursor2.execute(mySql_insert_query2, recordTuple)
        connection.commit()
        print("Record inserted successfully into Books")

    except mysql.connector.Error as error2:
        print("Failed to insert into MySQL table {}".format(error2))

    finally:
        if connection.is_connected():
            cursor2.close()
            connection.close()
            print("MySQL connection is closed")


def showBooks():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library_db',
                                             user='root',
                                             password='sukantahui')
        cursor = connection.cursor()
        mySql_insert_query = """select * from books"""
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mySql_insert_query)
        records = cursor.fetchall()
        print("Fetching each row using column name")

        for row in records:
            id = row["id"]
            name = row["book_name"]
            print(id, name)

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


project = "SBJW"
print("The platform is: ", os.name)
print("Welcome to ", project)
while True:
    print("Main Menu")
    print("1. book")
    print("2. Member")
    print("3. Transaction")
    print("4. Report")
    print("5. Exit")

    ch1 = int(input("Enter your Choice in Main Menu: "))
    if ch1 < 1 or ch1 > 5:
        print("Wrong choice ...............")
    if ch1 == 5:
        break
    if ch1 == 1:
        # Book area
        while True:
            print("\tBook Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t5. Exit")
            chBook = int(input("\tEnter your Choice in Book Menu: "))
            if chBook < 1 or chBook > 5:
                print("\tWrong choice in book menu ...............")
            if chBook == 5:
                break
            if chBook == 1:
                print(chBook)
                addBook("1234", "Suman Ghosh", "Dinesh", "ABP", 2020)
            if chBook == 4:
                showBooks()
