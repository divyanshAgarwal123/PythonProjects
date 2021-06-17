
from tkinter import *

root=Tk()
root.geometry("500x300")
def helloback():
    label1.config(text="hello divyansh")
label=Label(text="please Enter a first number")
label1=Label(text="please Enter a second number")
label2=Label(text="")
label2.place(x=200,y=20)
label.place(x=1,y=1)
label1.place(x=1,y=60)
button1 = Button(root,text="first number",fg="red",bg="yellow",height="2",width="13",command=helloback)
button1.place(x=2,y=20)
mainloop()
