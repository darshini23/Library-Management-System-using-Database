# to update BOOKS record
import sqlite3

bname = str(input("Enter the book name:"))
newstock = int(input("Enter the Stock:"))

# database connection for update record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "UPDATE BOOKS SET STOCK '%d' WHERE BNAME = '%s'" % (bname,newstock)
curs.execute(qry)
conn.commit()
print("Records Updated")