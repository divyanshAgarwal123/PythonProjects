def show():
    num_set=set([0,1,2,3,4,5])
    num_set.pop()
    print(num_set)
    num_set.pop()
    print(num_set)
    num_set.pop()
    print(num_set)
def diplay():
    num_set=set([0,1,2,3,4,5])
    num_set.discard(3)
    print(num_set)
show()
diplay()