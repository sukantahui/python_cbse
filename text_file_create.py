# this is text file creation
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sukantahui",
  database="metal_db"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
print(" ********************************** Tables ********************")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

print(" ********************************** all ledgers ********************")

mycursor.execute("SELECT * FROM ledgers")

myresult = mycursor.fetchall()


for x in myresult:
    print(x)

print(" ********************************** only one ledgers ********************")

mycursor.execute("SELECT * FROM ledgers where id=1")

myresult = mycursor.fetchone()


for x in myresult:
    print(x)