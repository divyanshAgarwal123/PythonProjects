grocery=["chips","juices","apple","lays","choclate"]
grocery.sort()
print(grocery)
print(grocery[4])
num=[12,4,2,6,21,3,8,0,7,1,5]
#num.sort()
#num.reverse()
#print(num[::-2])
#print(num[0:5])
num.insert(4,15)
#num.remove(21)
num.pop()
num[1]=98                                        #mutable = can change
print(num)                                       #immutable = can not change
helloguys=[]
helloguys.append("14")
helloguys.append("34")
helloguys.append("13")
print(helloguys)
tp=(45,)    #tuple    # it is immutable
#tp[1]=98
print(tp)
"""
a=7
b=4
temp=a
a=b             #traditnol way
b=temp
print(a,b)
"""
a=7
b=4
a , b = b , a           #python way
print(a,b)
print(a)