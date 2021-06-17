"""
50<2ruppes
50>1rupees
100>0.50
"""
x=int(input("enter your calls"))
if(x<51):
    print("your bill is ",x*2,"ruppes")
elif(x>50 and x<100):
    print("your bill is " ,x,"ruppes")
if(x>100):
    print("your bill is ",x * 0.50,"ruppes")

