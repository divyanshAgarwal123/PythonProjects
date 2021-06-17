x=input("enter a any name")
y=input("enter the alphabet you want to skip")
for val in x:

    if(val==y):
        continue
    print(val,end="")

print("\nbye bye")