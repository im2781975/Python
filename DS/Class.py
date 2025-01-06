class MultiIndexingList:    
    def __init__(self, value):        
        self.value = value           
    def __repr__(self):       
        return repr(self.value)       
    def __getitem__(self, item):        
        if isinstance(item, (int, slice)):            
            return self.__class__(self.value[item])        
        return [self.value[i] for i in item]      
    def __setitem__(self, item, value):      
        if isinstance(item, int):            
            self.value[item] = value    
        elif isinstance(item, slice):            
            raise ValueError('Cannot interpret slice with multiindexing')        
        else:           
            for i in item:                
                if isinstance(i, slice):                    
                    raise ValueError('Cannot interpret slice with multiindexing')                
                self.value[i] = value       
    def __delitem__(self, item):        
        if isinstance(item, int):            
            del self.value[item]        
        elif isinstance(item, slice):            
            del self.value[item]        
        else:           
            if any(isinstance(elem, slice) for elem in item):               
                raise ValueError('Cannot interpret slice with multiindexing')           
            item = sorted(item, reverse=True)            
            for elem in item:               
                del self.value[elem]
a = MultiIndexingList([1,2,3,4,5,6,7,8])
a[4, 1, 5:, 2, ::2]
a[4] = 1000
a[2,6,1] = 100
del a[5]
del a[4,2,5]

arr = ['a', 'b', 'c', 'd']
print(arr[0])
print(arr[1])
print(arr[-1])

class Integer(object):   
    def __init__(self, value):        
        self.value = int(value) # Cast to an integer           
    def __repr__(self):        
        return '{cls}({val})'.format(cls=self.__class__.__name__,   val=self.value)      
    def __pow__(self, other, modulo=None):        
        if modulo is None:           
            print('Using __pow__')            
            return self.__class__(self.value ** other)       
        else:            
            print('Using __pow__ with modulo')            
            return self.__class__(pow(self.value, other, modulo))      
    def __float__(self):        
        print('Using __float__')        
        return float(self.value)       
    def __complex__(self):        
        print('Using __complex__')       
        return complex(self.value, 0)
Integer(2) ** 2                 
Integer(2) ** 2.5               
pow(Integer(2), 0.5)            
operator.pow(Integer(2), 3)     
operator.__pow__(Integer(3), 3) 
pow(Integer(2), 3, 4)  
Integer(2).__pow__(3, 4)   

import math
math.pow(Integer(2), 0.5)
import cmath
cmath.exp(Integer(2)) 

z = y ** (1.0 / 3)

class sparselist(object):   
    def __init__(self, size):       
        self.size = size        
        self.data = {}      
    def __getitem__(self, index):        
        if index < 0:            
            index += self.size        
        if index >= self.size:           
            raise IndexError(index)
        try:            
            return self.data[index]        
        except KeyError:            
            return 0.0
    def __setitem__(self, index, value):       
        self.data[index] = value
    def __delitem__(self, index):        
        if index in self.data:            
            del self.data[index]
    def __contains__(self, value):        
        return value == 0.0 or value in self.data.values()
    def __len__(self):        
        return self.size
    def __iter__(self):        
        return (self[i] for i in range(self.size))
l = sparselist(10 ** 6) 
0 in l  
l[12345] = 10

class adder(object):  
    def __init__(self, first):        
        self.first = first  
    def __call__(self, second):       
        return self.first + second
add2 = adder(2) 
add2(1) 
add2(2)  

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

class AssignValue(object):    
    def __init__(self, value):        
        self.value = value 
my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value))
class Example(object):    
    def __init__(self,a,b,c):        
        self.a, self.b, self.c = a,b,c    
    def __format__(self, format_spec):       
    """ Implement special semantics for the 's' format specifier """        
        if format_spec[-1] != 's':            
            raise ValueError('{} format specifier not understood for this object', format_spec[:-1])
            raw = "(" + ",".join([str(self.a), str(self.b), str(self.c)]) + ")"
        return "{r:{f}}".format( r=raw, f=format_spec )
inst = Example(1,2,3)
print "{0:>20s}".format( inst )
class Person(object):  
    first = 'Zaphod'    
    last = 'Beeblebrox' 
'{p.first} {p.last}'.format(p=Person())

root
- A  
    - AA 
    - AB
- B 
    - BA
    - BB    
        - BBA
root = get_root(tree)
for node in get_children(root):    
    print(get_name(node))    
    for child in get_children(node):       
        print(get_name(child))        
        for grand_child in get_children(child):            
            print(get_name(grand_child))
def list_tree_names(node):    
    for child in get_children(node):       
        print(get_name(child))        
        list_tree_names(node=child) 
list_tree_names(node=get_root(tree))

def list_tree_names(node, lst=[]):    
    for child in get_children(node):        
        lst.append(get_name(child))        
        list_tree_names(node=child, lst=lst)    
    return lst
list_tree_names(node=get_root(tree))
