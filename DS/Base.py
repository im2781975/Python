def input_number(msg, err_msg=None):    
while True:       
    try:
        return float(raw_input(msg))        
    except ValueError:            
        if err_msg is not None:                
            print(err_msg) 
def input_number(msg, err_msg=None):
    while True:        
        try:            
            return float(input(msg))       
        except ValueError:      
            if err_msg is not None:                
            print(err_msg)
print("Hello, ", end="\n") 
print("World!")
print("Hello, ", end="") 
print("World!")
print("Hello, ", end="<br>")
print("World!")
print("Hello, ", end="BREAK")
print("World!")

try:   
    x = 1.0 / 0.0    
    print(x) 
except ZeroDivisionError:   
    print("Division by zero")

from collections import Counter
c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
c["a"]
Counter({"e": "e"}) 

from collections import Counter
adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
Counter(adict.values()).most_common()
Counter(adict.values()).most_common(1)
Counter(adict.values()).most_common(2)

alist = [1, 2, 3, 4, 1, 2, 1, 3, 4]
alist.count(1)
atuple = ('bear', 'weasel', 'bear', 'frog')
atuple.count('bear')
atuple.count('fox')

astring = 'thisisashorttext' 
astring.count('t')
astring.count('th')
astring.count('is')
astring.count('text')
from collections import Counter 
Counter(astring)

import numpy as np 
a=np.array([0,3,4,3,5,4,7]) >>> 
print np.sum(a==3)

d1 = {1:[]}
d2 = d1.copy()
d1 is d2
d1[1] is d2[1]

import copy 
c = [[1,2]]
d = copy.copy(c) 
c is d
c[0] is d[0]

import copy 
c = [[1,2]] 
d = copy.deepcopy(c) 
c is d
c[0] is d[0]

l1 = [1,2,3]
l2 = l1[:] 
l2
l1 is l2

s1 = {()} 
s2 = s1.copy() 
s1 is s2
s2.add(3)

def two_sum(a, b):
    return a + b
print(two_sum(2, 1)) 
print(two_sum("a", "b"))

def two_sum(a: str, b: str): 
    return a + b
def two_sum(a: int, b: int) -> int: 
    return a + b
import typing 
Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
import typing
T = typing.TypeVar("T")
def get_first_element(l: typing.Sequence[T]) -> T:  
    """Gets the first element of a sequence."""   
    return l[0]

div = int(input("Divisors of: ")) 
for x in range(div+1):
if div/x == div//x:      
    print(x, "is a divisor of", div)

div = int(input("Divisors of: ")) 
for x in range(1,div+1):
if div/x == div//x:      
    print(x, "is a divisor of", div)
    
for i in range(4):   
    d = i * 2 
print(d)

def noaccess():
    for i in range(4):    
        d = i * 2 
noaccess()

set1, tuple1 = {1,2}, (3,4) a = 
set1 + tuple1
b = 400 + 'foo'
c = ["a","b"] - [1,2]

def switch(value):   
    if value == 1:
        return "one"   
    if value == 2:       
        return "two"    
    if value == 42:       
        return "the answer to the question about life, the universe and everything"    
    raise Exception("No case found!")
switch(1)

switch = {    1: lambda: 'one',    2: lambda: 'two',    42: lambda: 'the answer of life the universe and everything', }
def default_case():    
    raise Exception('No case found!')
switch.get(1, default_case)()

def run_switch(value):    
    return switch.get(value, default_case)()
run_switch(1)

class SwitchBase:    
    def switch(self, case):       
        m = getattr(self, 'case_{}'.format(case), None)        
        if not m:            
            return self.default        
        return m
    __call__ = switch
    
class CustomSwitcher:    
    def case_1(self):        
        return 'one'    
    def case_2(self):        
        return 'two'    
    def case_42(self):        
        return 'the answer of life, the universe and everything!'    
    def default(self):       
        raise Exception('Not a case!')
switch = CustomSwitcher()
print(switch(1))
print(switch(2))

class Switch:   
    def __init__(self, value):       
        self._val = value    
    def __enter__(self):      
        return self    
    def __exit__(self, type, value, traceback):       
        return False # Allows traceback to occur    
    def __call__(self, cond, *mconds):       
        return self._val in (cond,)+mconds
def run_switch(value):   
    with Switch(value) as case:       
        if case(1):           
            return 'one'        
        if case(2):           
            return 'two'       
        if case(3):           
            return 'the answer to the question about life, the universe and everything'   
         raise Exception('Not a case!')
run_switch(1)

a, b = (1, 2)
print(a)
print(b)
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

l = [1, 2, 3, 4, 5]
head = l[0]
tail = l[1:]
a, b, *other, z = [1, 2, 3, 4, 5] 
print(a, b, z, other)

a, _ = [1, 2] 
print(a)
a, _, c = (1, 2, 3) 
print(a)

a, *_ = [1, 2, 3, 4, 5] print(a)
a, *_, b = [1, 2, 3, 4, 5] print(a, b)
a, _, b, _, c, *_ = [1, 2, 3, 4, 5, 6] print(a, b, c)

def fun1(arg1, arg2, arg3):    
    return (arg1,arg2,arg3)
fun1(1, 2, 3)
def fun2(arg1='a', arg2='b', arg3='c'):    
    return (arg1,arg2,arg3)
fun2(1)
fun2(1, 2) 
fun2(arg2=2, arg3=3)
l = [1,2,3]
fun1(*l)
fun1(*['w', 't', 'f'])
fun1(*['oops'])
d = {  'arg1': 1,  'arg2': 2,  'arg3': 3 } fun1(**d)
fun1(**{'arg1':1, 'arg2':2})
fun1(**{'arg1':1, 'arg2':2, 'arg3':3, 'arg4':4})
fun2(**d)
fun2(**{'arg2': 2})
fun2(**{'arg1':1, 'arg2':2, 'arg3':3, 'arg4':4})

def fun3(arg1, arg2='b', arg3='c')    
    return (arg1, arg2, arg3)
fun3(*[1])
fun3(*[1,2,3])
fun3(**{'arg1':1})
fun3(**{'arg1':1, 'arg2':2, 'arg3':3})
fun3(*[1,2], **{'arg3':3})
fun3(*[1,2], **{'arg2':42, 'arg3':3})

def fun1(*args, **kwargs):    print(args, kwargs)
fun1(1,2,3)
fun1(a=1, b=2, c=3)
fun1('x', 'y', 'z', a=1, b=2, c=3)

class MyString(str):   
    def __init__(self, *args, **kwarg):        
        print('Constructing MyString')        super(MyString, self).__init__(*args, **kwarg)

from operator import truediv, floordiv 
assert truediv(10, 8) == 1.25            
assert floordiv(10, 8) == 1     

first, second, *tail, last = [1, 2, 3, 4, 5]
print(first)
print(second)
print(tail)
print(last)

first, second, *tail, last = [1, 2, 3, 4]
print(tail)
first, second, *tail, last = [1, 2, 3]
print(tail)
print(last)
