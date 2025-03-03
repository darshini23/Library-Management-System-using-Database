# Inserting the students record

import sqlite3


sname = str(input("Enter the Student name:"))
rollno = int(input("Enter the Student Rollno:"))
dept = str(input("Enter the  Student Department:"))
year = int(input("Enter the pursuing year"))
bname = str(input("Enter the book to borrow:"))
date = str(input("Date of Borrowing:"))

# database connection to insert students record

conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "INSERT INTO students(SNAME,ROLLNO,DEPT,YEAR,BNAME,DATE) VALUES('%s','%d','%s','%d','%s','%s')" % (sname,rollno,dept,year,bname,date)
curs.execute(qry)
conn.commit()
print("Records added")