from tkinter import *
obj=Tk()
obj.geometry("800x600")
obj.resizable(width=False, height=False)
#labels
label0=Label(text="XYZ.Private Limited",font=("bold",20))
label0.place(x=250,y=1)
label=Label(text="Enter the name of the product",font=("bold",15))
label.place(x=1,y=50)
label1=Label(text="Enter the price of the product",font=("bold",15))
label1.place(x=1,y=100)
label2=Label(text="Enter the discount you get on product",font=("bold",15))
label2.place(x=1,y=200)
label3=Label(text="",font=("bold",13))
label3.place(x=1,y=300)
label4=Label(text="",font=("bold",13))
label4.place(x=1,y=400)
label5=Label(text="",font=("bold",13))
label5.place(x=250,y=400)
label6=Label(text="",font=("bold",13))
label6.place(x=1,y=450)
label7=Label(text="",font=("bold",13))
label7.place(x=250,y=450)
label8=Label(text="Enter The Quantity",font=("bold",15))
label8.place(x=1,y=150)
label9=Label(text="",font=("bold",13))
label9.place(x=1,y=350)
label10=Label(text="",font=("bold",13))
label10.place(x=250,y=350)

#textbox
product=Text()
product.place(x=400,y=50,width=200,height=30)
price=Text()
price.place(x=400,y=100,width=200,height=30)
discount=Text()
discount.place(x=400,y=200,width=200,height=30)
quantity=Text()
quantity.place(x=400,y=150,width=200,height=30)
def show():
    input  = product.get("1.0",'end-1c')
    input1 = price.get("1.0",'end-1c')
    input2 = discount.get("1.0",'end-1c')
    input3 = quantity.get("1.0",'end-1c')
    x = int(input1)
    y = int(input2)
    z=int(input3)
    a=y/100*x
    b=x-a
    e=b*z
    c=15/100*b
    d=b+c
    f=d*z
    label3.config(text="name of the product is:\t"+input)
    label4.config(text="your total price before GST is:")
    label5.config(text=e)
    label6.config(text="your total price after GST is:")
    label7.config(text=f)
    label9.config(text="QUANTITY:")
    label10.config(text=""+input3)
#button area
button=Button(obj,text="find money to pay",width=25,height=2,fg="red",bg="yellow",command=show)
button.place(x=400,y=250)
mainloop()