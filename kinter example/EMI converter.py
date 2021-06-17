from tkinter import *
obj=Tk()
obj.geometry("500x300")
obj.title("EMI CONVERTER")
def show():
    inputValue = T1.get("1.0", 'end-1c')
    inputValue1 = T2.get("1.0", 'end-1c')
    inputValue2 = T3.get("1.0", 'end-1c')
    x=int(inputValue)
    z=int(inputValue1)
    y=int(inputValue2)
    a=x*y*z//100
    b=x+a
    c=y*12
    d=b//c
    label3.config(text=d)
label=Label(text="Enter your Principle",font=("bold",15))
label.place(x=1,y=50)
label1=Label(text="Enter Rate Of Interest",font=("bold",15))
label1.place(x=1,y=100)
label2=Label(text="Enter your Time",font=("bold",15))
label2.place(x=1,y=150)
label3=Label(text="",font=("bold",15))
label3.place(x=1,y=200)
T1=Text()
T1.place(x=200,y=50,width=150,height=30)
T2=Text()
T2.place(x=200,y=100,width=150,height=30)
T3=Text()
T3.place(x=200,y=150,width=150,height=30)
button = Button(obj, text="convert", fg="red", bg="yellow", height="2", width="13",command=show)
button.place(x=200, y=250)
mainloop()