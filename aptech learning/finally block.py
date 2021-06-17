class A():
    def show(self):
        try:
            a=10/0
            print(a)
        except ArithmeticError as v:
            print("first",v)
        finally:
            print("code to be executed")
obj=A()
obj.show()