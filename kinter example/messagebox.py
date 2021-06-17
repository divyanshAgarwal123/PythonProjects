from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("100x200")
def show():
    msg=messagebox.showinfo("message box","hello python,hello world")
button=Button(obj,text="message",command=show)
button.place(x=1,y=1)
obj.mainloop()