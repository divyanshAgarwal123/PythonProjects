class A():
    def show(self):
        try:
            a=10
            print(a)
            raise NameError("hello")
        except NameError as e:
            print("an error occured")
            print(e)
obj=A()
obj.show()