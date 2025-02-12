print({x: x * x for x in (1, 2, 3, 4)})
print(dict((x, x * x) for x in (1, 2, 3, 4)))
print({name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6})
print(dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6))
print({x : x**2 for x in [1, 2, 3, 4, 5]})
print({x : x**3 for x in range(10) if x**3 % 4 == 0})
lst = "GFG"
print({x : { y: x + y for y in lst} for x in lst})
state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H' }
print(state['A'], "\n", state.keys(), "\n", state.values())
for key in state.keys():
    print('{} is the cap of {}'.format(state[key], key))
from collections import defaultdict
lst = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')] 
clt = defaultdict(list) 
for key, val in lst: 
    clt[key].append(val)
print(clt, end = " ")
state = defaultdict(lambda : 'Boston',{
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H' })
print(state['X'], "\n", state.keys(), "\n", state.values())
for key, value in state.items():
    print(key, value, end = " ")
dic = defaultdict(int)
print(dic['key'])
dic['key'] = 5; print(dic['key'])
dic = defaultdict(lambda : 'empty')
print(dic['key']); dic['key'] = 'full'
print(dic['key'])
dic = dict() 
dic['xyz'] = 123; dic['abc'] = 345
for i in dic :
    print("%s  %d" %(i, dic[i]))
dic = {}  
dic.setdefault('Another_key', []).append("This worked!"); print(dic)
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"} 
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
print({**fish, **dog})
from collections import ChainMap 
print(dict(ChainMap(fish, dog)))
dic = {'apple': 1, 'banana': 2} 
dec = {'coconut': 1, 'date': 1, 'apple': 3}
combined = ChainMap(dic, dec) 
reverse = ChainMap(dec, dic)
for key, val in combined.items():    
    print(key, val, end = " ")
for key, val in reverse.items():
    print(key, val, end = " ")
from itertools import chain 
print(dict(chain(fish.items(), dog.items())))
fish.update(dog); print(fish)

from itertools import groupby
from operator import itemgetter
adict = {'a': 1, 'b': 5, 'c': 1}
print(min(adict), max(adict), sorted(adict))
print(min(adict.items()), max(adict.items()), sorted(adict.items()))
print({ key : dict(items) for key, items in groupby(sorted(adict.items(), key = itemgetter(1)), itemgetter(1))})
print({ key: dict(items) for key, items in groupby(sorted(adict.items(), key = lambda x : x[1]), lambda x : x[1])})
alist_of_tuples = [(5,2), (1,3), (2,2)] 
print(sorted(alist_of_tuples, key = itemgetter(1,0)))
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),    ("vehicle", "speed boat"), ("vehicle", "school bus")]
things = [["animal", "bear"],["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], ["vehicle", "speed boat"],["vehicle", "school bus"]]
dic = {} 
func = lambda x: x[0]
for key, group in groupby(sorted(things, key = func), func):
    dic[key] = [item[1] for item in group]
print(dic, end = " ")
lst = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {} 
for key, val in lst:
    dic[key] = list(val)
print(dic, end = " ")
lst = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),'wombat', 'mongoose', 'malloo', 'camel']
#tes = sorted(lst, key = lambda x : x[0])
#c = groupby(tes, key = lambda x : x[0])
c = groupby(lst, key = lambda x : x[0])
dic = {}
for key, val in c:    
    dic[key] = list(val) 
print(dic, end = " ")

guy = [
    {'name' : 'A', 'age' : 12}, {'name' : 'B', 'age' : 17},
    {'name' : 'C', 'age' : 15}, {'name' : 'D', 'age' : 22}]
print(list(filter(lambda x : x['age'] < 20, guy)))
print(list(filter(lambda x : x['age'] % 2 == 0, guy)))
info = {'name' : 'A', 'add' : 'B', 'age' : 22, 'job' : 'C'}
info['lang'] = 'python'; info['name'] = 'x'
print(info, info['name'], info.keys(), info.values())
for key, value in info.items():
    print(key, value, end = " ")
key = ['a', 'b', 'c', 'd', 'e']
value = [1, 2, 3, 4, 5]
print({k : v for (k, v) in zip(key, value)})
print(dict.fromkeys(range(5), True))
num = {'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56}
num = dict({'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56})
num = dict([('A', 23), ('B', 34), ('C', 45)])
num['D'] = {23, 34, 45}
num['E'] = {'Home': 'Dhaka', 'contact': '234567'}; print()
print(num.keys(), num.values(), num.items())
print(num, num['A'], num.get('B'))
for key, value in num.items():
    print(key, value, end = " ")
for i in num:
    print(i, num[i], end = " ")
for i in num.items():
    print(i, end = " ")
for key in num:
    print(key, num[key], end = " ")
for key in num.keys():
    print(key, end = " ")
for val in num.values():
    print(key, ":", val, end = " ")
for key, val in num.items():
    print(key, ":", val, end = " ")
print([key for key in num])
print({key: value for key, value in num.items() if key == 'B'})
num = {"one": 1, "two": 2, "three": 3}
print({v : k for k, v in num.items()})
print(dict((v, k) for k, v in num.items()))
print(dict(zip(num.values(), num.keys())))
print(dict(map(reversed, num.items())))
cpy = num.copy(); print(cpy, len(cpy))
dic = {1 : [], 2 : set()}
#tuple is immuteable
cpy = dic.copy(); cpy[1].append(2);
cpy[2].add(5); print(cpy, dic is cpy, dic[1] is cpy[1])
info = {1 : 'abc', 2 : 'bcd', 3 : 'cde'}
print(info[1], info.keys(), info.values(), info.items())
del info[1]
print(info.popitem(), info.popitem())
info.clear(); print(info)
info = {
    "A" : {"roll" : 23, "age" : 22, "course" : "python"},
    "B" : {"roll" : 12, "age" : 24, "course" : "java", "num" : [234, 876]} }
info["A"]["num"] = 789
print(info["A"].pop("num"))
print(info, info["A"], info["B"]["num"])
#del info["A"]["num"]
stock = {'eggs': 5, 'milk': 2}
dic = {}
dic['eggs'], dic['milk'] = 5, 2
print(stock, dic)
dic = [('eggs', 5), ('milk', 2)]; print(dict(dic))
print(dict(eggs = 5, milk = 2))
print(dict.fromkeys(("milk", "eggs")))
print(dict.fromkeys(("milk", "eggs"), (2, 5)))
print(dict([('d', 4), ('e', 5), ('f', 6)]))
print(dict([('a', 1)], b = 2, c = 3))
print(dict({'a' : 1, 'b' : 2}, c = 3))
dic = {'Name' : 'Asam', 1 : [2, 3, 4]}
dic = {}
dic = dict({1 : 'Aa', 2 : 'Bb', 3 : 'Cc'})
dic = dict([(1, 'Aa'), (2, 'Bb')])
dic = {1 : 'Aa', 2 : 'Bb', 3 : {4 : 'Dd', 5 : 'Ee'}}
dic[6] = 'Ff'; dic[7] = 'Gg'; dic['Add'] = 2, 4, 9
dic[8] = {'Nested' : {'1' : 'Welcome', '2': 'Here'}}
print(dic[1], dic[2], dic[3], dic.get(3))
for key, value in dic.items():
    print(key, value, end = "\n")
dic = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}
print(dic, dic['Dict1'][1]); del(dic['Dict1'])
car = {}; car["wheels"] = 4
car["color"] = "Red"; car["model"] = "Corvette"
print("Little " + car["color"] + " " + car["model"] + "!")
car = {"wheels": 4, "color": "Red", "model": "Corvette"}
for key in car:  
    print(key + ": " + str(car[key]), end = " ")
duck = {1 : "python", 2 : " java", 3 : "Ruby"};
dic = duck.copy(); duck.clear(); dic.pop(2)
print(dic.items(), dic.keys(), dic.values())
dic.popitem(); dic.update({2 : "cpp"})
print(dic)
dic = {"1" : "B", '2' : 'C'}
print(dic.keys(), all(dic.keys()), dic.values(), all(dic.values())); print(sorted(dic))
dic = dict(); dic = dict(key = 'value')         
dic = dict([('key', 'value')])
dec = {'val' : 'val'}; dic = dict(**dec)
dic['newkey'] = 42; dic['newlist'] = [1, 2, 3] 
dic['newdict'] = {'nested_dict' : 1}
del dic['newkey']
print(dic)
dic = {}; print(dic)
print(dic.get("foo", "bar")); print(dic)
print(dic.setdefault("foo", "bar")); print(dic)
key = 'baz'; default= 'default'
try:
    value = dic[key]
except KeyError:
    value = default
print(f"Value for key '{key}' using try-except:", value) 
key = 'foo'
value = dic[key] if key in dic else default
print(f"Value for key '{key}' using if-else:", value)  
print(dic.get("unknown", "missing"))
print(dic.setdefault("foo", "newvalue"), dic)
print(dic.setdefault("newkey", "hello"), dic)

from collections import OrderedDict as Od
from operator import itemgetter
dic = {"Foo" : 3, "Baz" : 4}; dic["Bar"] = 9
print(dic.keys(), dic.values())
Od([("Tmp", 5), ("Tic", 6), ("Tec", 7)])
exp = Od()
exp['key1'] = "val1"; exp['key2'] = " val2"
exp = Od([("A", 1), ("B", 2)])
print(dic, exp)
dic = Od([('1st', 1), ('2nd', 2), ('3rd', 3)])
print([k for k in dic])
print({*range(4), 5, *(5, 6, 7)})
dic = ([('1st', 1), ('2nd', 2), ('3rd', 3)])
print(dic, [k for k in dic])
def func(**kwargs):
    print(kwargs.keys(), kwargs.values(), kwargs.items())
func(a = 1, b = 2, c = 3)
tail = {'y' : 7, 'z' : 5}; combined = {'x' : 1, **tail}
print(combined)
dic = {'a': 1, 'b': 5, 'c': 1}
res = Od(sorted(dic.items()))
print(res, res['a'])
print(min(dic.items(), key = lambda x : x[1]))
print(max(dic.items(), key = itemgetter(1)))
print(sorted(dic.items(), key = itemgetter(1), reverse = True))
dic = {'key': 6, 'other_key': 7} 
print("My other key is: {0[other_key]}".format(dic))
person = {'first': 'Arthur', 'last': 'Dent'} 
print('{p[first]} {p[last]}'.format(p = person))
dic = {'x' : 1, 'y' : 2}; dec = {'y' : 3, 'z' : 4}
print({**dic, **dec})
print({k : v for d in [dic, dec] for k, v in d.items()})
dic = {'a' : 1, 'b' : 2, 'c' : 3, '!' : 4}
tmp = [k for k in dic.keys() if k.isalpha()]
for key in tmp:
    del dic[key]
for key, value in dic.items():
    print(key, value)
print(sorted((7, 2, 1, 5)), sorted(['c', 'A', 'b']), sorted({11, 8, 1}))
print(sorted({'11': 5, '3': 2, '10': 15}), sorted('bdca'), sorted([2, 7, 5])[-1])
print(min(7,2,1,5), max(7,2,1,5), max([2, 7, 5]))
def getkey(dic, val):
    found = []
    for key in dic:
        if dic[key] == val:
            found.append(key)
    return found
    #return [key for key in dic if dic[key] == val]  
def getkeyComp(dic, val):
    return getkey(dic, val)  
def getOneKey(dic, val):
    return next((key for key in dic if dic[key] == val), "Value not found") 
dic = {'a': 10, 'b': 20, 'c': 10}
print(getkey(dic, 10))    
print(getkeyComp(dic, 10), getkeyComp(dic, 20))  
print(getkeyComp(dic, 25), getOneKey(dic, 10))   
print(getOneKey(dic, 20), getOneKey(dic, 25))

def outerIdx(seq, value):
    for index, inner in enumerate(seq):
        if value in inner:
            return index
    return "Value not found"
def innerIdx(seq, value):
    for oindex, inner in enumerate(seq):
        if value in inner:
            return oindex, inner.index(value)  
    return "Value not found"
lst = [(4, 5, 6), (3, 1, 'a'), (7, 0, 4.3)]
print(outerIdx(lst, 6), outerIdx(lst, 'a')) 
print(outerIdx(lst, 4.3), outerIdx(lst, 9))
print(innerIdx(lst, 'a'), innerIdx(lst, 7), innerIdx(lst, 99))  
def parrot(voltage, state, action): 
    print("This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.", end = ' ') 
    print("E's", state, "!")
dic = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**dic))
