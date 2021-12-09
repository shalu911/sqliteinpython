import sqlite3
filename =input("enter the database" )
tablename=input("please enter the table")
stu_name=input("please enter the student name")
stu_contact=input("please enter the student surname")
#always open the file
filename=filename+"sqlite3"
fo=open(filename,"a")
#always open the db connection
con=sqlite3.connect(filename)
cur=con.cursor
#create a table
cur.execute('CREATE TABLE'+tablename'(name text,surname text)')
cur.execute("INSERT INTO "+tablename+"(name,surname) VALUES('"+stu_name"','"+stu_surname+"')"")
#insert the student data
itrableobject=cur.execute('select *FROM'+tablename)
for row in iteableobject:
      print(row)
      con.commit()
      #always close the file
      fo.close()







fo=open(filename)