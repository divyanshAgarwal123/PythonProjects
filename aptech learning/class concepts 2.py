class A:
    def show(self):
        x=int(input("enter a number"))
        y = int(input("enter a number"))
        return x+y
class B(A):
    def display(self):
        result=B.show(3)
        print(result)
obj=B()
obj.display()
