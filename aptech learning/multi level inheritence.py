class A:
    def show(self):
        x=int(input("enter a number"))
        return x
class B(A):
    def display(self):
        y = int(input("enter a number"))
        return y
class C(B):
    def result(self):
        a=C.show(0)
        b=C.display(0)
        return a+b
class D(C):
    def printresult(self):
        x=C.result(0)
        print(x)
obj=D()
obj.printresult()



