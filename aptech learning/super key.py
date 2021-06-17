class A():
    def show(self):
        x = int(input("enter your principle"))
        y = int(input("enter your time"))
        print("rates are 8.5")
        return x * y * 8.5 // 100


class B(A):
    def display(self):

        a=super().show()
        print(a)




obj = B()
obj.display()