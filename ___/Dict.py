state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H',
}
print(state['A'])
print(state.keys(), state.values())
for key in state.keys():
    print('{} is the capital of {}'.format(state[key], key))
#defaultdict
from collections import defaultdict
stateCapital = defaultdict(lambda: 'Boston',{
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H',
})
print(stateCapital['X'])
"""                    """
actress = [
    {'name' : 'A', 'age' : 12}, {'name' : 'B', 'age' : 17},
    {'name' : 'C', 'age' : 15}, {'name' : 'D', 'age' : 22}
    ]
junior = filter(lambda x : x['age'] < 20, actress)
fiver = filter(lambda x : x['age'] % 2 == 0, actress)
print(list(junior), list(fiver))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = set(number)
num.add(10)
if 5 in num: num.remove(5)
print(num)
for i, item in enumerate(num):
    print(i, item)
A, B = {1, 2, 3}, {3, 4, 5, 6, 7, 8}
print(f"A & B: {A & B}\nA | B: {A | B} ")
comb = {}
comb = {(x, y)for x in A for y in B}
print(comb)
info = {'name' : 'A', 'Add' : 'B', 'age' : 22, 'job' : 'C'}
print(info, info['name'])
print(info.keys(), info.values())
info['lang'] = 'python'
info['name'] = 'X'
for key, value in info.items():
    print(key, value)
    
#num = {'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56}
#num = dict({'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56})
#Duplicate key will be ovverride
num = dict([('A', 23), ('B', 34), ('C', 45)])
num['D'] = {67, 78, 89}
num['B'] = {'Home' : 9876, 'work' : 5462}
num['A'] = 12
print(f"num: {num}\nnum['A']: {num['A']}\nnum['B']['work']: {num['B']['work']}\nnum.get(B): {num.get('B')}\n")
for i in num:
    print(i)
    print(num[i])
#print tuple
for i in num.items():
    print(i)
#copy dict
cpy = num.copy()
print(cpy, len(cpy))

Data = { 1 : 'abc', 2 : 'bcd', 3 : 'cde'}
print(f"data[1]: {Data[1]}\ndata.keys(): {Data.keys()}\ndata.values(): {Data.values()}\ndata.items(): {Data.items()} ")
del Data[2] #For delete data
print(Data.popitem())
print(Data.popitem())
Data.clear() #For.clear dict
print(Data)
"""					"""
Data = {
    "A" : {"roll" : 23, "age" : 22, "course" : "python"},
    "B" : {"roll" : 12, "age" : 24, "course" : "java", "num" : [234, 876]}
}
Data["A"]["num"] = 789
del Data["A"]["num"]
#print(Data["A"].pop("num"))
print(f"Data: {Data}\nData[A]: {Data['A']}\nData[B][num]: {Data['B']["num"]} ")

#declaration
dic = {'Name' : 'Asam', 1 : [2, 3, 4]}
dic = {}
dic = dict({1 : 'Aa', 2 : 'Bb', 3 : 'Cc'})
dic = dict([(1, 'Aa'), (2, 'Bb')])
dic = {1 : 'Aa', 2 : 'Bb', 3 : {4 : 'Dd', 5 : 'Ee'}}
dic[6] = 'Ff'
dic[7] = 'Gg'
dic['Add'] = 2, 4, 9
dic[8] = {'Nested' : {'1' : 'Welcome', '2': 'Here'}}
print(dic)
dic = {1 : 'Aa', 2 : 'Bb', 3 : 'Cc'}
print(dic[1], dic[2], dic[3], dic.get(3))
dic = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}
print(dic['Dict1'][1])
del(dic['Dict1'])
print(dic)
"""                """
dic = {1 : "python", 2 : " java", 3 : "Ruby"};
dic2 = dic.copy()
dic.clear()
print(dic2.items(), dic2.keys(), dic2.values())
dic2.pop(2)
print(dic2)
dic2.popitem(), dic2.update({2 : "scala"})
print(dic2.values())
"""                    """
dic = {"1" : "B", '2' : 'C'}
print(dic.keys(), all(dic.keys()), dic.values(), all(dic.values()))
print(sorted(dic))
"""					"""
from collections import OrderedDict
dic = OrderedDict([("A" ,  1), ("B" ,  2)])
dic = {"foo" : 5, "baz" : 7}
dic["bar"] = 9
print(dic)
OrderedDict([('foo', 5), ('bar', 6), ('baz', 7), ('foobar', 8)])
o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)
"""				"""
from collections import OrderedDict as od
dec = od([('first', 1), ('second', 2), ('third', 3)])
print([k for k in dec])
unique = {*range(4), 4, *(5, 6, 7)}
print(unique)
dec = {'first' : 1, 'second' : 2, 'third' : 3}
print(dec)
print([k for k in dec])
def func(**kwargs):
    print(kwargs.keys())
func(a = 1, b = 2, c = 3, d = 4, e = 5)
tail = {'y' : 7, 'z' : 5}
combined = {'x' : 1, **tail}
print(combined)
dic = {'x' : 1, 'y' : 2}
dec = {'y' : 3, 'z' : 4}
print({**dic, **dec})
dec = {'a' : 1, 'b' : 2, 'c' : 3, '!' : 4}
Delete = [key for key in dec.keys() if key.isalpha()]
for key in Delete:
    del dec[key]
for key,value in dec.items():
    print(key, value)
"""				"""
def getkey(dic, val):
    found = []
    for key in dic:
        if dic[key] == val:
            found.append(key)
    return found
def getkeyComp(dic, val):
    return [key for key in dic if dic[key] == val]
def getOneKey(dic, val):
    try:
        return next(key for key in dic if dic[key] == val)
    except StopIteration:
        return "Value not found"
dic = {'a': 10, 'b': 20, 'c': 10}
print(getkey(dic, 10))  
print(getkeyComp(dic, 10))  
print(getkeyComp(dic, 20))  
print(getkeyComp(dic, 25))  
print(getOneKey(dic, 10))  
print(getOneKey(dic, 20))  
print(getOneKey(dic, 25))  
def outerIdx(seq, value):
    try:
        return next(index for index, inner in enumerate(seq) for item in inner if item == value)
    except StopIteration:
        return "Value not found"
lstTup = [(4, 5, 6), (3, 1, 'a'), (7, 0, 4.3)]
print(outerIdx(lstTup, 'a'))  
print(outerIdx(lstTup, 4.3))  
print(outerIdx(lstTup, 99))  
def innerIdx(seq, value):
    try:
        return next((oindex, iindex) for oindex, inner in enumerate(seq) for iindex, item in enumerate(inner) if item == value)
    except StopIteration:
        return "Value not found"
print(innerIdx(lstTup, 'a'))  
print(innerIdx(lstTup, 7))    
print(innerIdx(lstTup, 99))   
"""				"""
print()
from collections import Counter
cnt = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(cnt["a"])
dec = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
print(Counter(dec.values()).most_common())
print(Counter(dec.values()).most_common(1))
import typing
Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
p1 = Point(3, 4)
print(f"Point coordinates: ({p1.x}, {p1.y})")
x, y = p1
print(f"x: {x}, y: {y}")
print(p1)
T = typing.TypeVar("T") 
def get_first_element(elements: typing.List[T]) -> T:
    if elements:
        return elements[0]
    raise ValueError("List is empty")
lst = [1, 2, 3]
strlst = ["apple", "banana", "cherry"]
print(get_first_element(lst)) 
print(get_first_element(strlst))

from operator import truediv, floordiv
assert truediv(10, 8) == 1.25
assert floordiv(10, 8) == 1

from datetime import datetime,timedelta   
once = datetime(2010, 7, 1, 12, 0, 0) 
delta = timedelta(days = 13, hours = 8,  minutes = 20)   
gen = (once + x * delta for x in range(5))
print('\n'.join(map(lambda d: d.strftime('%Y-%m-%d %H:%M:%S'), gen)))
print('North America: {dt:%m/%d/%Y}.  ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()))

import unicodedata
print([unicodedata.name(char) for char in "ê"])  
print([unicodedata.name(char) for char in "e"])  
print(unicodedata.normalize("NFKD", "ê")  == unicodedata.normalize("NFKD", "e"))
def normalize_caseless(text):    
    return unicodedata.normalize("NFKD", text.casefold())
def caseless_equal(left, right):    
    return normalize_caseless(left) == normalize_caseless(right)
"""            """
print(sorted((7, 2, 1, 5)), sorted(['c', 'A', 'b']), sorted({11, 8, 1}), sorted({'11': 5, '3': 2, '10': 15}), sorted('bdca'), min(7,2,1,5), max(7,2,1,5), max([2, 7, 5]), sorted([2, 7, 5])[-1])
dic = {1 : []}
dec = dic.copy()
print(dic is dec, dic[1] is dec[1])
dic = {()}
dec = dic.copy(); dec.add(2)
print(dic is dec)
dic = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic.keys(), dic.values(), dic.items())
for key in dic:
    print(key, end = " ")
for key in dic:
    print(key, dic[key], end = " ")
for key in dic.keys():
    print(key, end = " ")
for val in dic.values():
    print(key, ":", val, end = " ")
for key, val in dic.items():
    print(key, ":", val, end = " ")
print([key for key in dic])
from collections import defaultdict
dic = defaultdict(int)  
print("Initial access to 'key' (default int):", dic['key'])  
dic['key'] = 5
print("After setting 'key' to 5:", dic['key']) 
dic = defaultdict(lambda: 'empty')  
print("Initial access to 'key' (default lambda):", dic['key'])  
dic['key'] = 'full'  # Set value for 'key' to 'full'
print("After setting 'key' to 'full':", dic['key']) 
dic = {}  
dic.setdefault('Another_key', []).append("This worked!")  
print("After setdefault and append:", dic)

dic = dict()                  
dic = dict(key = 'value')         
dic = dict([('key', 'value')])
otherdict = {'existing_key': 'existing_value'}
dic = dict(**otherdict)  
dic['newkey'] = 42
dic['new_list'] = [1, 2, 3] 
dic['new_dict'] = {'nested_dict' : 1}
del dic['newkey']
print("After deleting 'newkey':", dic)

mydict = {}
print("Initial dictionary:", mydict)
print("Get 'foo' with default value 'bar':", mydict.get("foo", "bar"))
print("Dictionary after using get():", mydict)
print("Set default for 'foo' with value 'bar':", mydict.setdefault("foo", "bar"))
print("Dictionary after using setdefault():", mydict)
key = 'baz'
default_value = 'default'
try:
    value = mydict[key]
except KeyError:
    value = default_value
print(f"Value for key '{key}' using try-except:", value)
key = 'foo'
if key in mydict:
    value = mydict[key]
else:
    value = default_value
print(f"Value for key '{key}' using if-else:", value)

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"} 
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
from collections import ChainMap 
print(dict(ChainMap(fish, dog)))
from itertools import chain 
print(dict(chain(fish.items(), dog.items())))
fish.update(dog) 
print(fish)
dic = {"Hello": 1234, "World": 5678}
print(dic["Hello"], dic.get("whatever"), dic.get("whatever", "nuh - nuh"))

stock = {'eggs': 5, 'milk': 2}
dic = {}
dic['eggs'], dic['milk'] = 5, 2
print(stock, dic)
dec = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
dec['a'].append(4) 
dec['b'].append('four')
print(dec)

iterable = [('eggs', 5), ('milk', 2)] 
dic = dict(iterable)
dic = dict(eggs = 5, milk = 2)
dic = dict.fromkeys(("milk", "eggs"))
dic = dict.fromkeys(("milk", "eggs"), (2, 5))
from collections import OrderedDict
dic = OrderedDict() 
dic ['first'], dic ['second'], dic ['third'], dic ['last'] = 1, 2, 3, 4
for key in dic :   
    print(key, dic[key], end = " ")
    
def parrot(voltage, state, action): 
    print("This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.", end = ' ') 
    print("E's", state, "!")
dic = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**dic))
dic = dict(a = 1, b = 2, c = 3)     
dic = dict([('d', 4), ('e', 5), ('f', 6)])  
dic = dict([('a', 1)], b = 2, c = 3)
dic = dict({'a' : 1, 'b' : 2}, c = 3)  

car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
print("Little " + car["color"] + " " + car["model"] + "!")
car = {"wheels": 4, "color": "Red", "model": "Corvette"}
for key in car:  
    print(key + ": " + str(car[key]), end = " ")
import itertools
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
print(combinations)

print({x: x * x for x in (1, 2, 3, 4)})
print(dict((x, x * x) for x in (1, 2, 3, 4)))
print({name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6})
print(dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6))
dic = {'x': 1, 'y': 2} 
print({key: value for key, value in dic.items() if key == 'x'})

dic = {1: 'a', 2: 'b', 3: 'c'}
print({v: k for k, v in dic.items()})
print(dict((v, k) for k, v in dic.items()))
print(dict(zip(dic.values(), dic.keys())))
print(dict(map(reversed, dic.items())))

dic = {'w': 1, 'x': 1} 
dec = {'x': 2, 'y': 2, 'z': 2}
print({k : v for d in [dic, dec] for k, v in d.items()})
print({**dic, **dec})

from itertools import groupby
from operator import itemgetter
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),    ("vehicle", "speed boat"), ("vehicle", "school bus")]
things = [["animal", "bear"],["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], ["vehicle", "speed boat"],["vehicle", "school bus"]]
dic = {} 
f = lambda x: x[0]
for key, group in groupby(sorted(things, key = f), f):
    dic[key] = [item[1] for item in group]
print(dic, end = " ")
lst = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {} 
for key, val in lst:
    dic[key] = list(val)
print(dic, end = " ")
lst = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),'wombat', 'mongoose', 'malloo', 'camel']
c = groupby(lst, key = lambda x: x[0])
dic = {}
for key, val in c:    
    dic[key] = list(val) 
print(dic)

lst = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), 'wombat', 'mongoose', 'malloo', 'camel'] 
sorted_list = sorted(lst, key = lambda x: x[0]) 
print(sorted_list) 
c = groupby(sorted_list, key=lambda x : x[0])
dic = {}
for key, val in c:   
    dic[key] = list(val)
print(dic, end = " ")

import collections
lst = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')] 
clt = collections.defaultdict(list) 
for key, val in lst: 
    clt[key].append(val)
print(clt, end = " ")

dic = {'apple': 1, 'banana': 2} 
dec = {'coconut': 1, 'date': 1, 'apple': 3}
combined_dict = collections.ChainMap(dic, dec) 
reversedict = collections.ChainMap(dec, dic)
for key, val in combined_dict.items():    
    print(key, val, end = " ")
for key, val in reversedict.items():
    print(key, val, end = " ")
    
adict = {'a': 1, 'b': 5, 'c': 1}
print({
    key: dict(items) for key, items in groupby(sorted(adict.items(), key=itemgetter(1)), itemgetter(1))})
print({
    key: dict(items) for key, items in groupby(sorted(adict.items(), key=lambda x: x[1]), lambda x: x[1])})
alist_of_tuples = [(5,2), (1,3), (2,2)] 
print(sorted(alist_of_tuples, key = itemgetter(1,0)))

dic = {'a': 3, 'b': 5, 'c': 1}
print(min(dic), max(dic), sorted(dic), min(dic.items()), max(dic.items()), sorted(dic.items()))

from collections import OrderedDict
from operator import itemgetter
dic = {'a': 1, 'b': 5, 'c': 1}
res1 = OrderedDict(sorted(dic.items()))
print("OrderedDict by keys:", res1)
print("Value of 'a':", res1['a'])
min_pair = min(dic.items(), key = lambda x: x[1])
print("Minimum by value:", min_pair)
max_pair = max(dic.items(), key = itemgetter(1))
print("Maximum by value:", max_pair)
desc = sorted(dic.items(), key = itemgetter(1), reverse = True)
print("Sorted by values (descending):", desc)
dic = {'key': 6, 'other_key': 7} 
print("My other key is: {0[other_key]}".format(dic))
person = {'first': 'Arthur', 'last': 'Dent'} 
print('{p[first]} {p[last]}'.format(p = person))

key = ['a', 'b', 'c', 'd', 'e']
value = [1, 2, 3, 4, 5]
print({k : v for (k, v) in zip(key, value)})
dic = dict.fromkeys(range(5), True)
print(dic)
print({x : x**2 for x in [1, 2, 3, 4, 5]})
print({x : x**3 for x in range(10) if x**3 % 4 == 0})
l="GFG"
print({ x: {y: x + y for y in l} for x in l })

print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
