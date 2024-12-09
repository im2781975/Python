collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for item in collection:    
    i1 = item[0]    
    i2 = item[1]    
    i3 = item[2]
for item in collection:
    i1, i2, i3 = item
for i1, i2, i3 in collection:
    
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for s in lst:    
    print s[:1]
for idx, s in enumerate(lst):    
    print("%s has an index of %d" % (s, idx))
for i in range(2,4):   
    print("lst at %d contains %s" % (i, lst[i]))
for s in lst[1::2]:    
    print(s) for i in range(1, len(lst), 2):
        print(lst[i])

lst=[[1,2,3],[4,5,6],[7,8,9]]
print (lst[0])
print (lst[1])
print (lst[2])
print (lst[0][0])
print (lst[0][1])
