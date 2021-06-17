a=[]
x=int(input("how many character you want"))
for i in range(0,x):
    y = input("enter your characters")
    a.append(y)
    print(y.lower())
    print(y.upper())
    print(y.isalpha())
    print(y.isalnum())
print(a)


