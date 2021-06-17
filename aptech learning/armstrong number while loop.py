x=int(input("please enter a number"))
sum=0
num=x
a=0
while(x>0):
    a=x%10
    sum+=a*a*a
    print(sum)
