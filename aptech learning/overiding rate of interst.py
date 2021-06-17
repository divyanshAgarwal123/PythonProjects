class A():
    def show(self):
        x=int(input("enter your principle"))
        y = int(input("enter your time"))
        print("rates are 8.5", x*y*8.5//100)
    
class B(A):
    def show(self):
        result=A.show(1)
        print(result)
        a=int(input("\nenter your principle"))
        b= int(input("enter your time"))
        print("rates are 9")
        return a * b * 9 // 100
class C(B):
    def show(self):
        result=B.show(1)
        print(result)
        a=int(input("\nenter your principle"))
        b= int(input("enter your time"))
        print("rates are 10.5")
        print("rate of interst is",a*b*10.5//100)

obj=C()
obj.show()