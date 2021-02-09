import pymysql
import datetime

def createDatabase():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS books")

    # Create table as per requirement
    sql = """CREATE TABLE books (
              id bigint unsigned NOT NULL AUTO_INCREMENT,
              serial varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              book_name varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              author varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              publisher varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              publication int unsigned DEFAULT NULL,
              issue_date datetime DEFAULT NULL,
              PRIMARY KEY (id)
            ) ENGINE=InnoDB"""
    cursor.execute(sql)


# createDatabase()


# adding book
def addBook2(serial, name, author, publisher, publication):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """insert into books (
                                   id
                                  ,serial
                                  ,book_name
                                  ,author
                                  ,publisher
                                  ,publication
                                ) VALUES (
                                  NULL, '%s','%s', '%s', '%s','%d'
                                )""" % (serial, name, author, publisher, publication)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        print("done")
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def showBooks():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM books"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            book_id = row[0]
            serial = row[1]
            book_name = row[2]
            author = row[3]
            publisher = row[4]
            publication = row[5]
            # Now print fetched result
            print("ID = %s,Serial = %s,Title = %s,Author = %s,Publisher = %s, Edition = %s" % (
                book_id, serial, book_name, author, publisher, publication))
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def updateBooks():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE BOOKS SET publication = publication + 1  WHERE id = '%s'"

    try:
        # Execute the SQL command
        cursor.execute(sql, (3))
        print('updated')
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print('unable to update')
        db.rollback()

    # disconnect from server
    db.close()


def deleteBooks(book_id):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM books WHERE id = '%d'" % (book_id)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        print("Book Deleted", book_id)
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


# addBook("1234", "Suman Ghosh", "Dinesh", "ABP", 2020)
# showBooks()

today = datetime.date.today()

addBook2("1234", "xSuman Ghosh", "Dinesh", "ABP", 2020)
showBooks()
updateBooks()
deleteBooks(7)
print(today)
