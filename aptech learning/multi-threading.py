from threading import *
class A(Thread):
    def run(self):
        for i in range (5):
            print("aptech")

class B(Thread):
    def run(self):
        for i in range (5):
            print("hello")
a=A()
b=B()
a.start()
b.start()
a.join()
b.join()
print("bye")