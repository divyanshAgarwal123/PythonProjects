
"""
1.50=0-50
50-100=3
100-150=4.5
"""
print("enter your electricity minutes(only minutes)")
x=int(input())
if(x<50 and x>1):
    print("your total bill is ",x*1.5)
elif(x<100 and x>49):
    y=1.5+3
    print("your total bill is ",x*y)
elif(x<151 and x>99):
    z=1.5+3+4
    print("your total bill is ",x*z)