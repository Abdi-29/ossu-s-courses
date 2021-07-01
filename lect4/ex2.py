'''
def g(y):
    print(x)
    print(x + 1)
    return x

x = 5
g(x)    
print(x)
'''
'''
def new_func(tuples):
    integers = ()
    strings = ()
    for i in tuples:
       integers += (i[0],)
       strings += (i[1],)
    return strings   

tuples = ((1, "a"), (2, "b"), (3, "c"))
(a) = new_func(tuples)
print(a[2])
'''

nested_list = [[[1], [2, 3]]]
print(len(nested_list))

