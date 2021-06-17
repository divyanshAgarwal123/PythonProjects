class A():
    def show(self):
        x=int(input("enter a number"))
        y = int(input("enter a number"))
        return x*y
class B(A):
    def show(self):
        a=A.show(0)
        print(a)
        a=int(input("enter a number"))
        b = int(input("enter a number"))
        print(a+b)


obj = B()
obj.show()
"""
8% rate of interst 9%,10.5%
"""