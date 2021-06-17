class A:
    def main(self):
        x = int(input("enter the marks of the subject"))
        y = int(input("enter the marks of the subject"))
        z = int(input("enter the marks of the subject"))
        print(x+y+z//3)
        a=x+y+z//3
        if(a<100 and a>90):
            print("your grade is A+")
        elif(a<89 and a>80):
            print("your grade is A")
        elif(a<79 and a>65):
            print("your grade is B")
        elif(a<64 and a>50):
            print("your grade is C")
        elif(a<49 and a>35):
            print("your grade is D")
        elif (a < 34):
            print("your grade is E")
obj=A()
obj.main()
"""
1st class
varribles call in 2nd class
"""
