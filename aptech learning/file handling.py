file=open("file handling.txt","w")
file.write("hello world ")
file.write("how are you")
file.close()
print("file write succesfull")
#2
file=open("file handling.txt","r")
#3
for i in file():
    print(i)
"""
append mode in file handling
"""