class MyIterable:    
    def __iter__(self):         return self    
    def __next__(self):
        pass
class MySequence:    
    def __getitem__(self, index):         
        if (condition):             raise IndexError        
        return (item)

ex1 = MyIterableClass() 
ex2 = MySequence() 
for (item) in (ex1): pass
for (item) in (ex2): pass

s = {1, 2}  
i = iter(s)  
a = next(i)  
b = next(i)

s = {1, 2, 3}
for a in s:    
    print a 
l1 = list(s)
l2 = [a * 2 for a in s if a > 2]  

def gen():    
    yield 1 
iterable = gen() 
for a in iterable:   
    print a
