a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=(input("enter + to add , -  to subtract , / divide , * to multiply"))
if(c=='+'):
    if(a==56 or a==9 and b==9 or b==56 ):
        print("the answer is 77")
    else:
        print("your answer is ",a+b)
elif(c=='-'):
    print("your answer is ",a-b)
elif(c=='*'):
    if(a==45 or a==3 and b==3 or b==45 ):
        print("the answer is 555")
    else:
        print("your answer is ",a*b)
elif(c=='/'):
    if(a==56 or a==6 and b==6 or b==56 ):
        print("the answer is 4")                               
    else:
        print("your answer is ",a/b)