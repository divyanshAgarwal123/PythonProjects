"""
1.if maths englis and scinece marks=
    180>test alligible

2.share cost =50
if we buy 100
wet 14%
security charge 0.5%
brokrage charge 20rupees
"""
x=int(input("enter your maths marks"))
y=int(input("enter your English marks"))
z=int(input("enter your Science marks"))
print("your total marks are",x+y+z)
b=x+y+z
if(b>140):
    print("you are alligible for test")
else:
    print("you are not alligible for test")
#2.
print("share cost is 50")
print("you buy 100")
print("additional charge are 14%,0.5%,20ruppes")
x=5000*14/100
y=5000*0.5/100
print("your total bill is ",x+y+20)
