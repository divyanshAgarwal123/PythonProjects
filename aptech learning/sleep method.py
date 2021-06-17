from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range (4):
            print("aptech")
            sleep(2)

class B(Thread):
    def run(self):
        for i in range (5):
            print("hello")
            sleep(2)
a=A()
b=B()
a.start()
sleep(2)
b.start()
