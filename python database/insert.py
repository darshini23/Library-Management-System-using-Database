#TO ADD STUDENT RECORD
import sqlite3
name=str(input("Enter the name:"))
dept=str(input("Enter the department:"))
rno=int(input("Enter the roll no:"))
fee=int(input("Enter the fee:"))

#connection for database

conn=sqlite3.connect("college.db")
curs=conn.cursor()
qry="INSERT INTO students (NAME,DEPT,RNO,FEE) VALUES ('%s','%s','%d','%d')" % (name,dept,rno,fee)
curs.execute(qry)
conn.commit()
print("Record added")


