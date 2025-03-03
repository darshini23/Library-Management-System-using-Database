# to view record

import sqlite3


sname = str(input("Enter the Student name:"))


# database connection
conn = sqlite3.connect("library.db")
curs = conn.cursor()
qry = "SELECT * FROM BOOKS"
curs.execute(qry)
res = curs.fetchall()
for i in res:
  print(i)
print("view records")