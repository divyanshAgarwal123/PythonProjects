#=set()
#print(type(s))
#s=set([1,2,3,4,5,6,7,8,9,0])
s=set()
s.add(1)
s.add(2)
#s1=s.union({1, 2, 3})
s1={3,4,}
#s1=s.intersection({1, 2, 3,4,5,6,7,8,9})
print(s.isdisjoint(s1))
