"""a=lambda b:b-10
print(a(20))
c=lambda e,f:e*f
print(c(2,4))
"""
def compute(n):
    return lambda x:x*n
result=compute(2)
print("the double of 15 is",result(15))
result=compute(3)
print("the double of 15 is",result(15))
result=compute(4)
print("the double of 15 is",result(15))
result=compute(5)
print("the double of 15 is",result(15))
result=compute(6)
print("the double of 15 is",result(15))
