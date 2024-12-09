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
