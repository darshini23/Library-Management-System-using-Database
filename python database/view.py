#TO VIEW STUDENT RECORDS
import sqlite3

rno=int(input("Enter the roll no:"))


#connection for database

conn=sqlite3.connect("college.db")
curs=conn.cursor()
qry="SELECT * FROM students"
#qry="SELECT * FROM students WHERE RNO='%d'" % (rno)
curs.execute(qry)
res=curs.fetchall()
#print("View Records")
'''for i in res:
  print(i)'''
#res=curs.fetchone()
#print(res)
#fees=res[4]
#print(fees)


