from tkinter import *
obj=Tk()
obj.geometry("500x300")
def show():
    inputValue1 = T2.get("1.0", 'end-1c')
    x="divyansh123"
    if (inputValue1==x):
        label2.config(text="WELCOME")
    else:
        label3.config(text="your password is wrong please try again")

label=Label(text="please enter your username",font=("bold",15))
label.place(x=1,y=1)
label1=Label(text="please enter your password",font=("bold",15))
label1.place(x=1,y=50)
label2=Label(text="",font=("bold",15))
label2.place(x=200,y=100)
label3=Label(text="",font=("bold",15))
label3.place(x=100,y=100)

T1=Text()
T1.place(x=250,y=1,width=150,height=30)
T2=Text()
T2.place(x=250,y=50,width=150,height=30)
button = Button(obj, text="CHECK", fg="red", bg="yellow", height="2", width="13",command=show)
button.place(x=200, y=250)
mainloop()
