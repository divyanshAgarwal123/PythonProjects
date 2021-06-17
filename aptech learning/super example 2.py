class A:
    def show(self):
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        c = int(input("enter a number"))

        if(a>b and a>c):
            print("the graeater number is ",a)
        elif (b>a and b >c):
            print("the graeater number is ", b)
        elif (c > b and  a < c):
            print("the graeater number is ", c)
class B(A):
    def display(self):
        print("this is B class and display method")
        super().show()
class C(A):
    def Metro(self):
        print("delhi metro is running in 60 kmph")
        super().show()
class D(C,B,A):
    def aptech(self):
        print("hello aptech")
        super().show()
b1=D()
b1.show()
b1.display()
b1.aptech()

