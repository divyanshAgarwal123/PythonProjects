class A():
    def show(self):
        x=int(input("enter a number"))
        return x
class B(A):
    def display(self):
        y=int(input("enter a number"))
        return y
class C(B):
    def answer(self):
        a=C.show(0)
        b=C.display(0)
        return a+b
class D(C):
    def printanswer(self):
        x=C.answer(0)
        print(x)
obj=D()
obj.printanswer()

class E():
    def hello(self):
        x=int(input("enter a number"))
        return x
class F(A):
    def hierarchy(self):
        y=int(input("enter a number"))
        return y
class G(E,F):
    def answer2(self):
        a=G.hello(0)
        b=G.hierarchy(0)
        print( a*b)
obj=G()
obj.answer2()