from tkinter import *
obj = Tk()
obj.geometry("600x400")
#when pressing button area
def helloback():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    inputValue2 = T3.get("1.0",'end-1c')
    x = int(inputValue)
    y = int(inputValue1)
    z = int(inputValue2)
    a = x*y*z/100
    c=x+a
    m=z*12
    b=c//m
    label.config(text="")
    label1.config(text="")
    label2.config(text="")
    label3.config(text=b)
    label4.config(text="The EMI is")
#label area
label=Label(text="Enter the principle",font=("bold",15))
label.place(x=1,y=1)
label1 = Label(text="Enter the Rate ",font=("bold",15))
label1.place(x=1,y=50)
label2 = Label(text="Enter the time",font=("bold",15))
label2.place(x=1,y=100)
label3 = Label(text=" ",font=("bold",15))
label3.place(x=300,y=150)
label4 = Label(text="",font=("bold",15))
label4.place(x=1,y=150)
#text area
T1=Text()
T1.place(x=300,y=1,width=200,height=30)
T2=Text()
T2.place(x=300,y=50,width=200,height=30)
T3=Text()
T3.place(x=300,y=100,width=200,height=30)
#button area
button1 = Button(obj,text="Find Rate of interest",fg="red",bg="yellow",height="2",width="20",command=helloback)
button1.place(x=100,y=300)
mainloop()
"""
BILL
product name 
price 
discount
before GST 
and After GST
"""
