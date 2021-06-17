from threading import *
class A(Thread):
    def run(self):
        for i in range(5):
            a=15
            b=13
            x=a+b
            print(x)
        self.show()
        self.display()
    def show(self):
        for i in range(5):
            a = 5
            b = 3
            y = a * b
            print(y)
    def dipslay(self):
        for i in range(5):
            a = 15
            b = 13
            z = a - b
            print(z)

a=A()
a.start()

