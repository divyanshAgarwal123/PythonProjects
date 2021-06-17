def show():
    #1
    print("enter the principle")
    x=int(input())
    print("enter the time")
    z=int(input())
    print("enter the rate is 8.5")
    return x*z*8.5//100

def main():
    result=show()
    print("the rate of intrest is",result)
    a=result+500
    print("\nthe principle is",a)
    print("enter the time")
    b = int(input())
    print("enter the rate is 9.5")
    print("the rate of intrest is :", a * b * 9.5//100)
main()
