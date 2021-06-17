
x=int(input("please enter a number"))
p=0
for i in range (1,x+1):
    if(x%i==0):
        p=p+1
if(p==2):
    print("its a prime number")
else:
    print("its not a prime number")
