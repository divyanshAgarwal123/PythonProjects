x=int(input("enter a number"))
num=x
z=0
while(x>0):
    y=x%10
    z=z*10+y
    x=x//10
print("reverse number is ",z)
if(z==num):
    print("its a planidrome number")
else:
    print("its not a planidrome number")
