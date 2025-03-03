#TO DELETE STUDENT RECORD
import sqlite3

rno=int(input("Enter the roll no:"))


#connection for database

conn=sqlite3.connect("college.db")
curs=conn.cursor()
qry="DELETE FROM students WHERE RNO='%d'" % (rno)
curs.execute(qry)
conn.commit()
print("Record deleted")


