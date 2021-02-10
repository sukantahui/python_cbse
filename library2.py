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
              member_id bigint unsigned DEFAULT NULL,
              issue_date datetime DEFAULT NULL,
              is_issued tinyint DEFAULT '0',
              PRIMARY KEY (id)
            ) ENGINE=InnoDB"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS members")

    sql = """CREATE TABLE members (
           id BIGINT UNSIGNED AUTO_INCREMENT,
           serial varchar(20) DEFAULT NULL,
           member_name VARCHAR(255),
           phone VARCHAR(20),
           doj DATETIME,
           display TINYINT DEFAULT '1',
           inforce TINYINT DEFAULT '1',
          PRIMARY KEY (id)
        ) ENGINE = InnoDB"""
    cursor.execute(sql)
    # adding self as a member
    now = datetime.datetime.utcnow()
    addMember(1, "self", "9143656893", now)


# createDatabase()


# adding book
def addBook(serial, name, author, publisher, publication, member_id):
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
                                  ,member_id
                                ) VALUES (
                                  NULL, %s,%s, %s, %s,%s,%s
                                )"""
    try:
        # Execute the SQL command
        cursor.execute(sql,(serial, name, author, publisher, publication,member_id))
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


def getBookBySerial(find_serial):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM books where serial = %s"
    try:
        # Execute the SQL command
        cursor.execute(sql, find_serial)
        # Fetch all the rows in a list of lists.
        row = cursor.fetchone()
        if row == None:
            return 0
        else:
            return row[0]

    except:
        return 0
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def updateBooks(update_book_id, name, author, publisher, publication):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "update books SET  book_name = %s ,author = %s,publisher = %s ,publication = %s  WHERE id = %s"

    try:
        # Execute the SQL command
        cursor.execute(sql, (name, author, publisher, publication, update_book_id))
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


# adding member functions
def addMember(in_serial,in_name,in_phone, in_date):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """insert into members (
           id
          ,serial
          ,member_name
          ,phone
          ,doj
        ) VALUES (NULL,%s,%s,%s,%s
        )"""
    try:
        # Execute the SQL command
        cursor.execute(sql,(in_serial,in_name,in_phone,in_date))
        # Commit your changes in the database
        print("Member added")
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


# addBook("1234", "Suman Ghosh", "Dinesh", "ABP", 2020)
# showBooks()

today = datetime.date.today()
# createDatabase()
# addBook("1234", "xSuman Ghosh", "Dinesh", "ABP", 2020)
# showBooks()
# updateBooks()
# deleteBooks(7)


project = "SBJW"
print("Welcome to ", project)
while True:
    print("Main Menu")
    print("1. book")
    print("2. Member")
    print("3. Transaction")
    print("4. Report")
    print("9. Exit")

    ch1 = int(input("Enter your Choice in Main Menu: "))
    if ch1 == 9:
        break
    elif ch1 < 1 or ch1 > 5:
        print("Wrong choice ...............")

    if ch1 == 1:
        # Book area
        while True:
            print("\tBook Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t9. Exit Book Menu")
            chBook = int(input("\tEnter your Choice in Book Menu: "))
            if chBook == 9:
                break
            elif chBook < 1 or chBook > 5:
                print("\tWrong choice in book menu ...............")

            if chBook == 1:
                serial = input("\t\tEnter book Serial: ")
                title = input("\t\tBook Title: ")
                author = input("\t\tAuthor Name: ")
                publisher = input("\t\tPublisher: ")
                edition = int(input("\t\tEdition: "))
                addBook(serial, title, author, publisher, edition,1)
            if chBook == 2:
                # showBooks()
                book_serial = input("\t\tEnter Book serial to search: ")
                book_id = getBookBySerial(book_serial)
                if book_id == 0:
                    print("This serial does not exist")
                else:
                    title = input("\t\tBook Title: ")
                    author = input("\t\tAuthor Name: ")
                    publisher = input("\t\tPublisher: ")
                    edition = int(input("\t\tEdition: "))
                    updateBooks(book_id, title, author, publisher, edition)
            if chBook == 3:
                book_serial = input("\t\tEnter Book serial to search for delete: ")
                book_id = getBookBySerial(book_serial)
                if book_id == 0:
                    print("This serial does not exist")
                else:
                    deleteBooks(book_id)
            if chBook == 4:
                showBooks()
    if ch1 == 2:
        while True:
            print("\tMember Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t9. Exit Member Menu")
            chMember = int(input("\tEnter your Choice in Member Menu: "))
            if chMember == 9:
                break
            elif chMember < 1 or chMember > 5:
                print("\tWrong choice in member menu ...............")

            if chMember == 1:
                serial = input("\t\tEnter Member Serial: ")
                name = input("\t\tMember Name: ")
                phone = input("\t\tPhone: ")
                now = datetime.datetime.utcnow()
                addMember(serial,name,phone,now)
