#inserting the BOOKS Record

import sqlite3
bname = str(input("Enter the bookname:"))
stock = int(input("Enter the Stock:"))

# Database Connection for inserting BOOKS Record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "INSERT INTO BOOKS(BNAME,STOCK) VALUES('%s','%d')" % (bname,stock)
curs.execute(qry)
conn.commit()
print("Records added") 