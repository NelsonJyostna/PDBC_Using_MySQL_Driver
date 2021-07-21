import MySQLdb
print("MySQLdb imported succesfully")
conn=MySQLdb.connect('localhost', 'root', 'NElson@26', 'pdbc')
print("connection estalablished Successfully")
curs=conn.cursor()
print("Cursor created")
sq1="SHOW DATABASES"
sq2="SHOW TABLES"
sq3="CREATE TABLE STUD(rn INT, name VARCHAR(20), MARKS INT)"
sq4="DESC stud"
#r=int(input("Enter Roll no"))
#n=input("Enter a name..")
#m=float(input("ENter a marks"))
#insert =f'insert into stud values({r},"{n}",{m})' 
update="UPDATE stud  SET MARKS=25 WHERE RN=1"
DELETE="DELETE FROM stud WHERE MARKS=25"
retrive='select * From stud' 
curs.execute(retrive)
for row in curs:
   print(row)
print("query executed")
conn.commit()
print("Connection commited")
curs.close()
print("cursor closed")
conn.close()
print("connection closed")
