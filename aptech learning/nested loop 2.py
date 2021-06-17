x=int(input("enter how many rows you want"))
n=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(n,"\t",end="")
        n=n+1
    print("")

