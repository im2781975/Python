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

