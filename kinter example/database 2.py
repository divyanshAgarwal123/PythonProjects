import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Root", database="company")
cur = myconn.cursor()
try:
    cur.execute("select * from detail")
    result = cur.fetchall()
    for x in result:
        print(x)
except:
    myconn.rollback()
myconn.close()
