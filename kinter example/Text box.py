from tkinter import *
obj=Tk()
obj.geometry("600x300")

def helloback():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    y=int(inputValue)
    x=int(inputValue1)
    label.config(text="")
    label1.config(text="")
    label3.config(text=y+x)
def show():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    y=int(inputValue)
    x=int(inputValue1)
    label.config(text="")
    label1.config(text="")
    label3.config(text=y-x)
def display():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    y=int(inputValue)
    x=int(inputValue1)
    label.config(text="")
    label1.config(text="")
    label3.config(text=y*x)
def hello():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    y=int(inputValue)
    x=int(inputValue1)
    label.config(text="")
    label1.config(text="")
    label3.config(text=y/x)


label=Label(text="please Enter a first number",font=("bold",15))
label1=Label(text="please Enter a second number",font=("bold",15))
label3=Label(text="",font=("bold",15))
label3.place(x=1,y=200)
T1=Text()
T1.place(x=300,y=1,width=200,height=30)
T2=Text()
T2.place(x=300,y=100,width=200,height=30)
label2=Label(text="")
label2.place(x=200,y=20)
label.place(x=1,y=1)
label1.place(x=1,y=100)
button1 = Button(obj,text="ADD",fg="red",bg="yellow",height="2",width="13",command=helloback)
button1.place(x=100,y=200)
button2 = Button(obj,text="SUBTRACT",fg="red",bg="yellow",height="2",width="13",command=show)
button2.place(x=200,y=200)
button3 = Button(obj,text="MULTIPLY",fg="red",bg="yellow",height="2",width="13",command=display)
button3.place(x=300,y=200)
button4 = Button(obj,text="DIVIDE",fg="red",bg="yellow",height="2",width="13",command=hello)
button4.place(x=400,y=200)
mainloop()
