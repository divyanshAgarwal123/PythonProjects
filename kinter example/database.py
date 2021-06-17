from tkinter import *
import mysql.connector
obj=Tk()
obj.geometry("600x400")
obj.title("REGISTRATION FORM")
hello=IntVar()
first=IntVar()
second=IntVar()
third=IntVar()
def show():
    gender = hello.get()
    if(gender == 1):
        gender = "male"
    elif(gender == 2):
        gender = "female"
    elif gender == 3:
        gender = "other"

    language = first.get()
    if (language == 1):
        language = "C"
    elif (language== 2):
        language = "C++"
    elif (language== 3):
        language = "PYTHON"

    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    myconn=mysql.connector.connect(host="localhost",user="root",passwd="Root",database="company")
    cur=myconn.cursor()
    sql="insert into detail(name,password,gender,language) values (%s,%s,%s,%s)"
    val=(inputValue,inputValue1,gender,language)
    try:
        cur.execute(sql,val)
        myconn.commit()
    except:
        myconn.rollback()

button = Button(obj, text="PRINT", fg="red", bg="yellow", height="2", width="13", command=show)
button.place(x=200, y=250)
#radio button
R1=Radiobutton(obj,text="MALE",variable=hello,value=1,command=button)
R1.place(x=200,y=150)
R2=Radiobutton(obj,text="FEMALE",variable=hello,value=2,command=button)
R2.place(x=200,y=175)
R3=Radiobutton(obj,text="OTHER",variable=hello,value=3,command=button)
R3.place(x=200,y=200)
label=Label(obj)
label.pack()
lbl1=Label(text="")
lbl1.pack(anchor=W)
#check box
R4=Checkbutton(obj,text="C",variable=first,onvalue=1,offvalue=0,command=button)
R4.place(x=250,y=150)
R5=Checkbutton(obj,text="C++",variable=first,onvalue=2,offvalue=0,command=button)
R5.place(x=250,y=175)
R6=Checkbutton(obj,text="PYTHON",variable=first,onvalue=3,offvalue=0,command=button)
R6.place(x=250,y=200)
#text box
T1=Text()
T1.place(x=200,y=1,width=150,height=30)
T2=Text()
T2.place(x=200,y=100,width=150,height=30)
label=Label(text="enter you name ",font=("bold",15))
label.place(x=1,y=1)
label2=Label(text="enter your password",font=("bold",15))
label2.place(x=1,y=100)
label3=Label(text="",font=("bold",15))
label3.place(x=400,y=1)
label4=Label(text="",font=("bold",15))
label4.place(x=400,y=100)

mainloop()