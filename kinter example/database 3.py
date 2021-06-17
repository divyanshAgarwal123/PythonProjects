import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Root", database="company")
cur = myconn.cursor()
try:
    cur.execute("delete from detail where name = 'dishu'")
    myconn.commit()
except:
    myconn.rollback()
myconn.close()