l=[10,20,30,40,50]
n=int(input("enter a number"))
for i in range(len(l)):
    if type(l[i])==int and l[i]==n:
        print("exists at position",i+1)
        break
else:
        print("does not exist")
