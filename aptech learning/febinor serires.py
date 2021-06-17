x=int(input("please enter a number"))
n1=0
n2=1
n3=0
i=2
print("",n1,"",n2,end="")
for i in range(2,x+1):
    n3=n1+n2
    print("",n3,end='')
    n1=n2
    n2=n3