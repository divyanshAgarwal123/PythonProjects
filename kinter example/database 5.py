import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Root", database="company")
cur = myconn.cursor()
sql="insert into detail(name,password,gender,language) values (%s,%s,%s,%s)"
val = [("john",2000.0,"male",210),("David",2500.0,"male",211),("Nick",4000.0,"male",212)]
try:
    cur.executemany(sql,val)
    myconn.commit()
    print(cur.rowcount,"records inserted!")
except:
    myconn.rollback()
myconn.close()