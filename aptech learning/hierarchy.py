class A():
    def show(self):
        x=int(input("enter a number"))
        return x

class B():
    def display(self):
        y=int(input("enter a number"))
        return y
class C(A,B):
    def result(self):
        a = B.display(0)
        b = C.display(0)
        print( a + b)
obj=C()
obj.result()
