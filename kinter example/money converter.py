from tkinter import *
import tkinter as tk
obj=Tk()
obj1=tk.Tk()
obj.geometry("500x300")
obj.title("MONEY CONVERTER")
bg_image = tk.PhotoImage(file="untitled1.png")
x = tk.Label(image=bg_image)
x.place(x=1,y=1)
def show():
    inputValue = T1.get("1.0", 'end-1c')
    x=inputValue
    z=float(x)
    y=z*74.25
    label2.config(text=y)

label=Label(text="Enter you money",font=("bold",15))
label.place(x=1,y=50)
label1=Label(text="$",font=("bold",15))
label1.place(x=350,y=50)
label2=Label(text="",font=("bold",15))
label2.place(x=200,y=100)
label3=Label(text="rupees",font=("bold",15))
label3.place(x=300,y=100)
T1=Text()
T1.place(x=200,y=50,width=150,height=30)
button = Button(obj, text="convert", fg="red", bg="yellow", height="2", width="13",command=show)
button.place(x=200, y=250)
mainloop()