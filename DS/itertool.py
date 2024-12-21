import itertools
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2)) 
b = list(itertools.combinations(a, 3))
print(b)

def is_even(x): 
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44] 
result = list(itertools.dropwhile(is_even, lst))
print(result)

def dropwhile(predicate, iterable):    
    iterable = iter(iterable)    
    for x in iterable:        
        if not predicate(x):            
            yield x            
            break    
        for x in iterable:        
            yield x
result = list(itertools.takewhile(is_even, lst)) + list(itertools.dropwhile(is_even, lst))

from itertools import zip_longest 
a = [i for i in range(5)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
for i in zip_longest(a, b):  
    x, y = i 
    print(x, y)
for i in zip_longest(a, b,fillvalue='Hogwash!'):   
    x, y = i  
    print(x, y)

results = fetch_paged_results()
limit = 20 
for data in itertools.islice(results, limit):   
    print(data)
    
def gen():    
    n = 0    
    while n < 20:        
        n += 1        
        yield n
for part in itertools.islice(gen(), 3):    
    print(part)
#itertools.islice(iterable, 1, 30, 3)

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
def testGroupBy(lst):    
    groups = itertools.groupby(lst, key=lambda x: x[1])   
    for key, group in groups:        
        print(key, list(group))
testGroupBy(lst)
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)] 
testGroupBy(lst)

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)] 
groups = itertools.groupby(lst, key=lambda x: x[1])
for key, group in sorted(groups):
    print(key, list(group))
    
groups = itertools.groupby(lst, key=lambda x: x[1]) 
for key, group in sorted((key, list(group)) for key, group in groups):   
    print(key, list(group))
    
def is_even(x):    
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44] 
result = list(itertools.takewhile(is_even, lst))
print(result)

def takewhile(predicate, iterable):    
for x in iterable:        
    if predicate(x):            
        yield x        
    else:            
        break
result = list(itertools.takewhile(is_even, lst)) + list(itertools.dropwhile(is_even, lst))

a = [1,2,3]
list(itertools.permutations(a))
list(itertools.permutations(a, 2))
set(itertools.permutations(a))

