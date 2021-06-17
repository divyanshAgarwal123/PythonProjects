from tkinter import *
obj = Tk()
obj.geometry("600x400")
def show():
    inputvalue=T1.get("1.0", 'end-1c')
    inputvalue1=T2.get("1.0", 'end-1c')
    x = int(inputvalue)
    y = int(inputvalue1)

    if(inputvalue > inputvalue1):
        z=x-y
        label2.config(text=z)
        label3.config(text="you have a profit of Rs")
    if(inputvalue < inputvalue1):
        z=y-x
        label2.config(text=z)
        label3.config(text="you have a loss of Rs")
label=Label(text="Enter the cost price",font=("bold",15))
label.place(x=1,y=1)
label1 = Label(text="Enter the selling price ",font=("bold",15))
label1.place(x=1,y=50)
label2 = Label(text="",font=("bold,15"))
label2.place(x=300,y=100)
label3 = Label(text="",font=("bold,15"))
label3.place(x=100,y=100)
T1=Text()
T1.place(x=300,y=1,width=200,height=30)
T2=Text()
T2.place(x=300,y=50,width=200,height=30)
button1 = Button(obj,text="Find Profit or Loss",fg="red",bg="yellow",height="2",width="20",command=show)
button1.place(x=100,y=300)
mainloop()