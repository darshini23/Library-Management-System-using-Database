#TO UPDATE STUDENT RECORD
import sqlite3

rno=int(input("Enter the roll no:"))
revfee=int(input("Enter the revised fee:"))

#connection for database

conn=sqlite3.connect("college.db")
curs=conn.cursor()
qry="UPDATE students SET FEE='%d' WHERE RNO='%d'" % (revfee,rno)
curs.execute(qry)
conn.commit()
print("Record Updated")


