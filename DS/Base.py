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

class Vector(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y) 
    def __sub__(self, v): 
        return Vector(self.x - v.x, self.y - v.y) 
    def __mul__(self, s): # Multiplication with a scalar. 
        return Vector(self.x * s, self.y * s) 
    def __div__(self, s):  
        float_s = float(s) return Vector(self.x / float_s, self.y / float_s)
    def __floordiv__(self, s):
        return Vector(self.x // s, self.y // s)
    def __repr__(self):
        return '<Vector (%f, %f)>' % (self.x, self.y, ) 
a = Vector(3, 5) 
b = Vector(2, 7)
print a + b
print b - a 
print b * 1.3 
print a // 17 
print a / 17 

from datetime import datetime,timedelta   
once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0) 
delta = timedelta(days=13, hours=8,  minutes=20)   
gen = (once_upon_a_time + x * delta for x in xrange(5))  
print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))
from datetime import datetime 
'North America: {dt:%m/%d/%Y}.  ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()) '

import unicodedata
[unicodedata.name(char) for char in "ê"]
[unicodedata.name(char) for char in "e"]
unicodedata.normalize("NFKD", "ê") == unicodedata.normalize("NFKD", "e")

import unicodedata
def normalize_caseless(text):    return unicodedata.normalize("NFKD", text.casefold())
def caseless_equal(left, right):    return normalize_caseless(left) == normalize_caseless(right)

d = {"a": 1, "b": 2, "c": 3}
for key in d:    
    print(key)
for key in d.keys():    
    print(key)
for key in d.iterkeys():    
    print(key)
for value in d.values():    
    print(value)
for key, value in d.items():    
    print(key, "::", value)

#buidin
d = dict()                  
d = dict(key='value')         
d = dict([('key', 'value')])
d = dict(**otherdict)  

#modify
d['newkey'] = 42
d['new_list'] = [1, 2, 3] 
d['new_dict'] = {'nested_dict': 1}
del d['newkey']

mydict = {}
print(mydict) 
print(mydict.get("foo", "bar"))
print(mydict) 
print(mydict.setdefault("foo", "bar"))
print(mydict)
try:
    value = mydict[key] 
except KeyError:    
    value = default_value
if key in mydict:   
    value = mydict[key]
else:    
    value = default_value
    
d = {'a': 1, 'b': 2, 'c':3}
for key in d:    
    print(key, d[key])
for key, value in d.items():    print(key, value)
for key, value in d.values():    print(key, value)
print([key for key in d])

from collections import defaultdict 
d = defaultdict(int)
d['key']                        
d['key'] = 5
d['key']                         
d = defaultdict(lambda: 'empty') 
d['key']                         
d['key'] = 'full'
d['key']          
d = {}
d.setdefault('Another_key', []).append("This worked!")

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"} 
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
from collections import ChainMap 
dict(ChainMap(fish, dog))
{'hands': 'fins', 'color': 'red', 'special': 'gills', 'name': 'Nemo'}
from itertools import chain 
dict(chain(fish.items(), dog.items())) 
{'hands': 'paws', 'color': 'red', 'name': 'Clifford', 'special': 'gills'}
fish.update(dog) 
print(fish)

mydict = { 'a': '1', 'b' : '2'}
print(mydict.keys())
print(mydict.values())
print(mydict.items())

dictionary = {"Hello": 1234, "World": 5678} 
print(dictionary["Hello"])
w = dictionary.get("whatever") 
x = dictionary.get("whatever", "nuh-uh")

stock = {'eggs': 5, 'milk': 2}
dictionary = {}
dictionary['eggs'] = 5 
dictionary['milk'] = 2
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
mydict['a'].append(4) 
mydict['b'].append('four')
iterable = [('eggs', 5), ('milk', 2)] 
dictionary = dict(iterables)
dictionary = dict(eggs=5, milk=2)
dictionary = dict.fromkeys((milk, eggs))
dictionary = dict.fromkeys((milk, eggs), (2, 5))

from collections import OrderedDict
d = OrderedDict() 
d['first'] = 1 
d['second'] = 2
d['third'] = 3 
d['last'] = 4
for key in d:   
    print(key, d[key])
    
def parrot(voltage, state, action): print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ') 
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"} >>> 
parrot(**d)

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"} 
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"} 
fishdog = {**fish, **dog} 
print(fishdog)

dict(a=1, b=2, c=3)     
dict([('d', 4), ('e', 5), ('f', 6)])  
dict([('a', 1)], b=2, c=3)
dict({'a' : 1, 'b' : 2}, c=3)  

car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
print "Little " + car["color"] + " " + car["model"] + "!"

car = {"wheels": 4, "color": "Red", "model": "Corvette"}
for key in car:  
    print key + ": " + car[key]
    

import itertools 
options = { "x": ["a", "b"],    "y": [10, 20, 30]}
keys = options.keys() 
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination))for combination in itertools.product(*values)]
print combinations

{x: x * x for x in (1, 2, 3, 4)}
dict((x, x * x) for x in (1, 2, 3, 4))

{name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6}  
dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6) 

initial_dict = {'x': 1, 'y': 2} 
{key: value for key, value in initial_dict.items() if key == 'x'}

my_dict = {1: 'a', 2: 'b', 3: 'c'}
swapped = {v: k for k, v in my_dict.items()}
swapped = dict((v, k) for k, v in my_dict.iteritems()) 
swapped = dict(zip(my_dict.values(), my_dict))
swapped = dict(zip(my_dict.values(), my_dict.keys()))
swapped = dict(map(reversed, my_dict.items()))
print(swapped)

dict1 = {'w': 1, 'x': 1} 
dict2 = {'x': 2, 'y': 2, 'z': 2}
{k: v for d in [dict1, dict2] for k, v in d.items()}
{**dict1, **dict2}

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),    ("vehicle", "speed boat"), ("vehicle", "school bus")]
dic = {} 
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):    
    dic[key] = list(group) 
dic

things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"],       ["vehicle", "speed boat"], ["vehicle", "school bus"]]
dic = {} 
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):   
    dic[key] = list(group)
dic

c = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {} 
for k, v in c:
    dic[k] = list(v)
dic
    
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),'wombat', 'mongoose', 'malloo', 'camel']
c = groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:    
    dic[k] = list(v) 
dic

list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), 'wombat', 'mongoose', 'malloo', 'camel'] 
sorted_list = sorted(list_things, key = lambda x: x[0]) 
print(sorted_list) 
print()
c = groupby(sorted_list, key=lambda x: x[0])
dic = {}
for k, v in c:   
    dic[k] = list(v)
dic

s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')] 
dd = collections.defaultdict(list) 
for k, v in s: 
    dd[k].append(v)
dd

dict1 = {'apple': 1, 'banana': 2} 
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}
combined_dict = collections.ChainMap(dict1, dict2) 
reverse_ordered_dict = collections.ChainMap(dict2, dict1)
for k, v in combined_dict.items():    
    print(k, v)
for k, v in reverse_ordered_dict.items():
    print(k, v)

from itertools import groupby 
from operator import itemgetter
adict = {'a': 1, 'b': 5, 'c': 1}
dict((i, dict(v))
for i, v in groupby(adict.items(), itemgetter(1)))
dict((i, dict(v)) for i, v in groupby(adict.items(), lambda x: x[1]))

alist_of_tuples = [(5,2), (1,3), (2,2)] 
sorted(alist_of_tuples, key=itemgetter(1,0))

adict = {'a': 3, 'b': 5, 'c': 1}
min(adict)
max(adict)
sorted(adict)
min(adict.items())
max(adict.items())
sorted(adict.items())
from collections import OrderedDict 
OrderedDict(sorted(adict.items()))
res = OrderedDict(sorted(adict.items()))
res['a']
min(adict.items(), key=lambda x: x[1])
max(adict.items(), key=operator.itemgetter(1))
sorted(adict.items(), key=operator.itemgetter(1), reverse=True)

list_of_tuples = [(0, 10), (1, 15), (2, 8)]
min(list_of_tuples)
min(list_of_tuples, key=lambda x: x[0]) 
min(list_of_tuples, key=lambda x: x[1]) 
sorted(list_of_tuples, key=lambda x: x[0])  
sorted(list_of_tuples, key=lambda x: x[1])  

import operator  
max(list_of_tuples, key=operator.itemgetter(0))
max(list_of_tuples, key=operator.itemgetter(1))
sorted(list_of_tuples, key=operator.itemgetter(0), reverse=True)
sorted(list_of_tuples, key=operator.itemgetter(1), reverse=True) 

max([], default=42)   
max([], default=0)  

sorted((7, 2, 1, 5))  
sorted(['c', 'A', 'b']) 
sorted({11, 8, 1})
sorted({'11': 5, '3': 2, '10': 15})
sorted('bdca')

import heapq
heapq.nlargest(5, range(10))
heapq.nsmallest(5, range(10))

min(7,2,1,5)
max(7,2,1,5)
max([2, 7, 5])
sorted([2, 7, 5])[-1]

class MyClass(object):    
    def __init__(self, value, name):        
        self.value = value        
        self.name = name           
    def __lt__(self, other):        return self.value < other.value       
    def __repr__(self):        return str(self.name)
sorted([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')]) 
max([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')]) 

my_dict = {'key': 6, 'other_key': 7} 
print("My other key is: {0[other_key]}".format(my_dict)) 
person = {'first': 'Arthur', 'last': 'Dent'} 
'{p[first]} {p[last]}'.format(p=person)
