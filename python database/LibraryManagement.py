#  PYTHON PROJECT IN LIBRARY MANAGEMENT SYSTEM 

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


# database connection to view  BOOKS records

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "SELECT * FROM BOOKS"
curs.execute(qry)
res = curs.fetchall()
for i in res:
  print(i)
print("view records") 

 # Inserting the students record

sname = str(input("Enter the Student name:"))
rollno = int(input("Enter the Student Rollno:"))
dept = str(input("Enter the  Student Department:"))
year = str(input("Enter the pursuing year"))
bname = str(input("Enter the book to borrow:"))
date = str(input("Date of Borrowing:")) 

# database connection to insert student record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "INSERT INTO student(SNAME,ROLLNO,DEPT,YEAR,BNAME,DATE) VALUES('%s','%d','%s','%s','%s','%s')" % (sname,rollno,dept,year,bname,date)
curs.execute(qry)
conn.commit()
print("Records added") 

# to update BOOKS record
bname= str(input("Enter the book name:"))
newstock = int(input("Enter the Stock:"))

# database connection for update record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "UPDATE BOOKS SET STOCK = '%d' WHERE BNAME = '%s'" % (newstock,bname)
curs.execute(qry)
conn.commit()
print("Records Updated") 

# database connection to view student Record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "SELECT * FROM student"
curs.execute(qry)
res = curs.fetchall()
for i in res:
  print(i)
print("view records") 



