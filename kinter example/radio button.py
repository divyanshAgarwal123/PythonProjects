from tkinter import *
def selection():
    gender=hello.get()
    if(gender==1):
        x="you are male"
        selection1 =x
        label.config(text="" + selection1)
    elif(gender==2):
        y="you are female"
        selection1 = y
        label.config(text="" + selection1)
    elif(gender==3):
        z="you are other"
        selection1 = z
        label.config(text="" + selection1)
obj = Tk()
obj.geometry("600x400")
hello=IntVar()
lbl=Label(text="GENDER CHECKBUTTON")
lbl.pack()
button=Button(obj,text="gender",bg="yellow",height="2",width="20",command=selection)
button.place(x=300,y=300)
R1=Checkbutton(obj,text="MALE",variable=hello,value=1,command=button)
R1.pack(anchor=W)
R2=Checkbutton(obj,text="FEMALE",variable=hello,value=2,command=button)
R2.pack(anchor=W)
R3=Checkbutton(obj,text="OTHER",variable=hello,value=3,command=button)
R3.pack(anchor=W)
label=Label(obj)
label.pack()
lbl1=Label(text="")
lbl1.pack(anchor=W)
obj.mainloop()