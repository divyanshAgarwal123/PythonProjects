from tkinter import *
master = Tk()
master.geometry("500x200")
button1 = Button(master,text="usrename",fg="red",bg="yellow",height="2",width="13")
button = Button(master,text="Login",fg="blue",bg="green",height="2",width="13")
button1.place(x=100,y=25)
button.place(x=100,y=100)
mainloop()