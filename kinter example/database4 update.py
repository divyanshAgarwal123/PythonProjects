import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Root", database="company")
cur = myconn.cursor()
try:
    cur.execute("update detail set password=4545 where name='divyas'")
    myconn.commit()
except:
    myconn.rollback()
myconn.close()