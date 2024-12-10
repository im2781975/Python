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

a = [1, 2, 3, 4, 5]
b = [8, 9]
a.append(6)
a.append(b)
a.extend(b)
a.insert(0, 0)
a.insert(2, 5)
a.extend(range(3))
a.index(7)
a.index(7, 8)
a.pop(2)
a.pop(8)
a.pop()
a.remove(9)
a.reverse()
a.count(7)
a.sort()
a.sort(reverse=True)
my_string = "hello world"
a.append(my_string)

a = [1, 2, 3, 4, 5, 6] + [7, 7] + b

import datetime
class Person(object):   
    def __init__(self, name, birthday, height):        
        self.name = name        
        self.birthday = birthday
        self.height = height   
    def __repr__(self):        return self.name
l = [Person("John Cena", datetime.date(1992, 9, 12), 175),     
Person("Chuck Norris", datetime.date(1990, 8, 28), 180),     
Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]
l.sort(key=lambda item: item.name)
l.sort(key=lambda item: item.birthday)
l.sort(key=lambda item: item.height)

import datetime
l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'height': 175}, {'name': 'Chuck Norris', 'birthday': 
    datetime.date(1990, 8, 28),'height': 180}, {'name': 'Jon Skeet', 'birthday': 
        datetime.date(1991, 7, 6), 'height': 185}]
l.sort(key=lambda item: item['name'])
l.sort(key=lambda item: item['birthday'])
l.sort(key=lambda item: item['height'])

import datetime
l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'size': {'height': 175, 'weight': 100}}, {'name': 'Chuck Norris', 'birthday': 
    datetime.date(1990, 8, 28),'size' : {'height': 180, 'weight': 90}}, {'name': 'Jon Skeet', 'birthday': 
        datetime.date(1991, 7, 6), 'size': {'height': 185, 'weight': 110}}] 
l.sort(key=lambda item: item['size']['height'])
        
from operator import itemgetter,attrgetter 
people = [{'name':'chandan','age':20,'salary':2000},          {'name':'chetan','age':18,'salary':5000},          {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age') 
by_salary = itemgetter('salary') 
people.sort(key=by_age)
people.sort(key=by_salary)

list_of_tuples = [(1,2), (3,4), (5,0)] 
list_of_tuples.sort(key=itemgetter(1)) 
print(list_of_tuples)

persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),           
Person("Chuck Norris", datetime.date(1990, 8, 28), 180),         
Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]
person.sort(key=attrgetter('name'))
by_birthday = attrgetter('birthday') 
person.sort(key=by_birthday) 

b = ["blah"] * 3
b.clear()
b = [1, 3, 5] * 5
a = list(range(10)) 
del a[::2] 
del a[-1] 
del a[:]

lst = [1, 2, 3, 4]
lst[-1]  
lst[-2]  
lst[-5]
lst[len(lst)-1]
lst[1:]      
lst[:3]      
lst[::2]     
lst[::-1]    
lst[-1:0:-1] 
lst[5:8]
lst[1:10]
lst[::-1] 
lst[3:1:-1] 
reversed(lst)[0:2]

data = 'chandan purohit    22 2000'
name_slice = slice(0,19)
age_slice = slice(19,21) 
salary_slice = slice(22,None)
print(data[name_slice]) 
print(data[age_slice])
print(data[salary_slice])

lst = []
if not lst:   
    print("list is empty")

my_list = ['foo', 'bar', 'baz']
for item in my_list:    
    print(item)
for (index, item) in enumerate(my_list):    
    print('The item in position {} is: {}'.format(index, item))
for i in range(0,len(my_list)):    print(my_list[i])
for item in my_list:    
    if item == 'foo':        
        del my_list[0]    
    print(item)

lst = ['test', 'twest', 'tweast', 'treast'] 
'test' in lst 
'toast' in lst
slst = set(lst)
'test' in slst

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):    print(a, b)

alist = ['a1', 'a2', 'a3'] 
blist = ['b1', 'b2', 'b3', 'b4']
for a, b in zip(alist, blist):    print(a, b)

alist = [] len(list(zip(alist, blist)))

alist = ['a1', 'a2', 'a3']
blist = ['b1'] 
clist = ['c1', 'c2', 'c3', 'c4'] 
for a,b,c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
    
alist = [123, 'xyz', 'zara', 'abc'] 
alist.insert(3, [2009]) print("Final List :", alist)

len(['one', [2, 3], 'four']) 
names = ["aixk", "duke", "edik", "tofp", "duke"] 
list(set(names))
import collections
collections.OrderedDict.fromkeys(names).keys()

alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
print(alist[0][0][1])
print(alist[1][1][2])
alist[0][0].append(11)
print(alist[0][0][2])
for row in alist:
    for col in row:       
        print(col)
[col for row in alist for col in row]
alist[1].insert(2, 15)
for row in range(len(alist)): 
    for col in range(len(alist[row])):       
        print(alist[row][col])
print(alist[1][1:])
print(alist)

my_list = [None] * 10 
my_list = ['test'] * 10
my_list=[{1}] * 10
print(my_list)
my_list[0].add(2)
print(my_list)
my_list=[{1} for _ in range(10)]

squares = [x * x for x in (1, 2, 3, 4)]
for x in (1, 2, 3, 4):    
    squares.append(x * x)
    
[s.upper() for s in "Hello World"]
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]

sentence = "Beautiful is better than ugly"
["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]

[x for x in 'apple' if x in 'aeiou' else '*']
[x if x in 'aeiou' else '*' for x in 'apple']

def foo(i):    
    return i, i + 0.5 
for i in range(3):    
    for x in foo(i):   
        yield str(x)
        
[str(x)   
    for i in range(3)      
        for x in foo(i) ]
        
[x.sort() for x in [[2, 1], [4, 3], [0, 1]]]
[sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]

[print(x) for x in (1, 2, 3)]

from random import randrange 
[randrange(1, 7) for _ in range(10)]

[x for x in range(10) if x % 2 == 0]

for x in range(10):   
    if x % 2 == 0:        even_numbers.append(x)
print(even_numbers)

[x if x % 2 == 0 else None for x in range(10)]
