import MySQLdb
print("MySQLdb imported succesfully")
conn=MySQLdb.connect('localhost', 'root', 'NElson@26', 'pdbc')
print("connection established Successfully")
curs=conn.cursor()
print("Cursor created")
sq1="SHOW DATABASES"
sq2="SHOW TABLES"
sq3="CREATE TABLE stud_info(rn INT, name VARCHAR(30), MARKS INT)"
sq4="DESC stud"


while True:
    ch=int(input("Enter ur choice : 1. Add \t 2. show \t 3.Update \t 4. Delete \t 5.Exist"))
    if ch==1:
        rn=int(input("Enter ur student roll no :"))
        name=input("Enter a student name")
        marks=int(input("Enter a marks :"))
        insert=f'insert into stud_info values({rn},"{name}",{marks})'
        curs.execute(insert)
        conn.commit()
    elif ch==2:
      curs.execute('select * from stud_info;')
      for row in curs:
          print(row)

    elif ch==3:
            ch_up=int(input("Enter ur choice : 1. update by name \t 2.update by marks"))
            if ch_up==1:
                 rnu=input("enter a new name you want to update :")
                 rno=int(input("Enter a roll no : "))
                 update=f'update stud_info set name="{rnu}" where rn={rno}'
                 print("Ur marks are updated by name")       
                 curs.execute(update)
                 conn.commit()
            elif ch_up==2:
                 rnmarks=int(input("enter a new marks you want to update : "))
                 rno=int(input("Enter a roll no : "))
                 update=f'update stud_info set marks={rnmarks} where rn={rno}'
                 print("ur marks r updated by marks")
                 curs.execute(update)
                 conn.commit()
    elif ch==4:
            ch_de=int(input("Enter ur choice : 1. delete by name \t 2.delete by marks"))
            if ch_de==1:
                 rnu=input("enter a new name you want to delete : ")
                 delete=f'delete from stud_info where name="{rnu}"'
                 print("Ur marks are delete by name")       
                 curs.execute(delete)
                 conn.commit()
            elif ch_de==2:
                 rno=int(input("Enter a new roll no you want to delete : "))
                 delete=f'delete from stud_info where rn={rno}'
                 print("ur marks r updated by marks")
                 curs.execute(delete)
                 conn.commit()
    elif ch==5:
          print("Executed succesfully")
          break

               
                  
#print("query executed")
conn.commit()
#print("Connection commited")
curs.close()
#print("cursor closed")
conn.close()
print("connection closed")
