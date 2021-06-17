"""with open("file handling.txt","r") as f:
    data=f.read()
    print(data)
    print(f.close())"""
def show():
    x=input("enter the texts")
    file=open("file handling.txt","a")
    file.write(x)
    file.close()
    file = open("file handling.txt")
    line = file.readline()
    print(line)
    print("file writing succesfull")
show()