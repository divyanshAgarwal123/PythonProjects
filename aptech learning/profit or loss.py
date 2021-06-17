x=int(input("enter the product price"))
y=int(input("enter the selling price"))
if(y>x):
    print("you have the profit of",y-x)
elif(y<x):
    print("you have the loss of",x-y)