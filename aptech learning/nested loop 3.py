x=int(input("enter numbers of rows"))
for i in range(x,0,-1):
    for j in range(i):
        print("*",end="")
    print("")