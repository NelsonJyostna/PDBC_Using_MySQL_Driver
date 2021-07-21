import MySQLdb
conn=MySQLdb.connect('localhost', 'root', 'NElson@26', 'advik')
curs=conn.cursor()

#d="create table employee(eid int primary key, ename varchar(20), eexp float, esal float, edesg varchar(20), eaddr varchar(20))"
#curs.execute(d)

while True:
    try:
      ch=int(input("Enter a choice : 1. Add \t  2. Show \t 3. Update \t 4. Delete \t 5. Exist"))
    except Exception as e:
        print("Exception occured", e)
        continue
    if ch==1:
       try: 
        id=int(input("enter ur id :"))
        name=input("Enter ur name :")
        exp=float(input("Enter ur experience :"))
        salery=float(input("Enter ur salery :"))
        desg=input("Enter ur designation :")
        addr=input("Enter ur address :")
        insert=f'INSERT INTO employee values({id}, "{name}", {exp}, {salery}, "{desg}", "{addr}")'
        curs.execute(insert)
        conn.commit()
       except Exception as e:
           print("Exception occured ", e)
           continue
    elif ch==2:
         curs.execute("select * from employee")
         #print("eid" \t  "ename" "exp" "salery" "edesg" "eaddr")
         
         for row in curs:
             print(row)
    elif ch==3:
        print("Update code")
        try: 
         ch_up=int(input("Enter a choice for update : \t 1. Update by name \t 2. Update by addr"))
        except Exception as e:
           print("Exception occured", e)
           continue
        if ch_up==1:
           try: 
            id1=int(input("Enter ur id :"))
            name =input("Enter ur NEW name :")
            update=f'UPDATE employee SET ename="{name}" where eid={id1}'
            curs.execute(update)
            conn.commit()
            print("Ur name is updated successfully")
           except Exception as e:
               print("Exception occured", e)
               continue
        elif ch_up==2:
           try:
            id2=int(input("Enter ur id :"))
            addres=input("Enter ur NEW address :")
            update=f'UPDATE employee SET eaddr="{addres}" where eid={id2}'
            curs.execute(update)
            conn.commit()
            print("Ur Address is updated successfully")
           except Exception as e:
               print("Exception occured", e)
               continue
        else:
            print(ch_up,"U have entered wrong choice")
            #continue
    elif ch==4:
          print("Delete code")
          try: 
           ch_de=int(input("Enter a choice for Delete : \t 1. Delete by name \t 2. Delete by addr"))
          except Exception as e:
             print("Exception occured", e)
             continue
          if ch_de==1:
             try: 
              name =input("Enter ur name :")
              delete=f'DELETE from employee where ename={name}'
              curs.execute(delete)
              conn.commit()
              print("Ur name is deleted successfully")
             except Exception as e:
                 print("Exception occured", e)
                 continue
          elif ch_de==2:
             try: 
              addres=input("Enter ur address :")
              delete=f'delete from where eaddr={addres}'
              curs.execute(delete)
              conn.commit()
              print("Ur Address is deleted successfully")
             except Exception as e:
               print("Exception occured", e)
               continue
          else:
             print(ch_de,"U have entered wrong choice")
             #continue
    elif ch==5:
         print("Existed succesfully")
         break
    else:
        print(ch,"You have entered wrong choice")


              

conn.commit()

curs.close()

conn.close()
print("connection closed")


