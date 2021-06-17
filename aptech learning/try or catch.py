class A():
    def show(self):
        try:
            a=10/g
            print(a)
        except ArithmeticError as v:
            print("first",v)
        except ZeroDivisionError:
            print("second")
        except Exception as e:
            print("third",e)
        else:
            print("hello")
obj=A()
obj.show()