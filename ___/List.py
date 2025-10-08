#list is Muteable
#Assign & access value 
x = y = [12, 13, 14]
x = [9, 10, 11]
y[0] = -1
print(f"x:{x}, y:{y}")
x = [1, 2, 3, [4, 5, 6], 7]
print(f"x:{x},\nx[3]:{x[3]}, \nx[3][2]:{x[3][2]} ")

lst = [1, 3.60, 'Hello', 'd']
tisl = ["Hello", "world"]
lst += tisl
print(lst, lst[0 : 2], lst * 2)
#insert
name = ['A', 'B', 'C', 'D', 'E']
name.insert(1, 'F')
print(len(name))
name.reverse()
if 'B' in name:
    name.remove('B')
for i in name:
    print(i)
print(name.count('A'))
print(f"name: {name}, \nname.index[F]: {name.index('F')} ")

l1 = [1, 2, 3, 4, 5]
l2 = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
for item in l1:
    for name in l2:
        print(item, name)
        if item == 4 and name == 'Cc':
            break
    print("Inner")
print("outer")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = []
for n in num:
    if n % 2 == 1:
        odd.append(n)
#odd = [n for n in num if n % 2 == 1 if n % 5 == 0]
print(odd)

player, age = ['A', 'B', 'C'], [21, 22, 23]
comb = []
for p in player:
    for a in age:
        comb.append([p, a])
#comb = [(p, a)for p in player for a in age]
print(comb)

number = [5, 10, 15, 20]
sum = 0
for num in number:
    sum += num
    print(num)
    if sum > 20:
        print(f"{sum} is Greater than 20")
print(sum)
for i in number[:]:
    sum += i
    number.append(sum)
print(number)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
E = map(lambda x : x * x, num)
print(list(E))
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"num[len(num) - 1]: {num[len(num) - 1]} ")
print(num[3], num[-3])
#start : end
print(f"num[:] {num[:]}\nnum[2:] {num[2:6]}\nnum[1:] {num[1:]}\nnum[:7] {num[:7]} ")
#start : end : range
print(f"num[1:8:1] {num[1:8:1]}\nnum[1:8:2] {num[1:8:2]}\nnum[2:8:-1] {num[2:8:-1]}\nnum[8:2:-1] {num[8:2:-1]}\nnum[8:2:-1] {num[8:2:-2]}\nnum[::-1] {num[::-1]} ")
num.append(100)
num.insert(6, -1)
if 5 in num: num.remove(5)
print(num)
if 6 in num:
    idx = num.index(6) 
    print(idx)
print(num.pop(), num)
num.sort() 
num.reverse()
print(num)
print(f"length is: {len(num)} ")
print(f"list is: {num}\nMaximum is: {max(num)}\nMinimum is: {min(num)} ")
num.append(45)
num.extend([46, 47, 48]) #For append more value
num[1] = -1 
num[2 : 4] = [49, 50, 51]
x = int(input("Enter integer: "))
if x in num: 
    num.remove(x)
else: 
    print("Doesn't exit")
print(num.sort()) #output : None
#num.remove(x) remove first occurance
print(num.pop())
print(num.pop(1))#num.pop(idx)
print(num.count(0))
print(num)
#nested
num = [1, 10, 15, [20, -10, 15], 17, -20]
print(len(num))
print(f"num[3][1]: {num[3][1]}\nnum[len(num) - 1]: {num[len(num) - 1]}\nnum[3][0 : 3]: {num[3][0 : 3]}\nnum[3][-1 : 3]: {num[3][-1: 3]}\nnum[3][::-1]: {num[3][::-1]}\n ")
num = [1, 10, 15, ["Aa", "Bb", "Cc"], 17, -20]
print(f"num[3][1]: {num[3][1]}\nnum[len(num) - 1]: {num[len(num) - 1]}\nnum[3][0 : 3]: {num[3][0 : 3]}\nnum[3][-1 : 3]: {num[3][-1: 3]}\nnum[3][::-1]: {num[3][::-1]}\n ")

lst = [1, 2, 3, 4, 5]
while(x := len(lst)) > 2:
    lst.pop()
    print(x, end = " ")
"""				"""
x, y = ["a", "b", "c", "d"], ["a", "b", "c", "d"] 
print(x is y)
if "b" in x:
    print("True")

lst = ["A", "B", " C"]
lst = []
lst = [10, 20, 30]
lst = ["A", 10, "B", 20, "C", 30]
lst = [["A", "B"], ["C", " D"]]
for i in range(1, 5):
    lst.append(i)
lst.append((7, 9))
tsil = ["Z", "X"]
tsil.append(lst)
print(tsil)
lst.insert(1, 7) #lst.insert(idx, val)
lst.extend([8, 'Geeks', 'Always'])
lst.reverse()
rev = list(reversed(lst))
print(rev)
print(lst[:], lst[-1], lst[::-1])
print(len(lst))

"""                """
string = input("Enter: ")
lst = string.split()
print(lst)
n = int(input("Enter integer: "))
lst = list(map(int, input("Enter the integer elements:").strip().split()))[:n]
print(lst)
"""            """
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(0, 5):
    if i in lst:
        lst.remove(i)
lst.pop(2)
print(lst.pop())
"""				"""
import operator, functools
lst = [1, 2, 3, 4]
print(lst, *lst)
print(functools.reduce(operator.truediv, lst))
import itertools
print(list(itertools.zip_longest([1, 2, 3], [1, 2], [1, 2, 3, 4])))
lst = [7, 'x', (1, 2), [5, 6], 5, 8.0, 'y', 1.2, [7, 8], 'z'] 
print(sorted(lst, key = str))
ing = 'Hello world'
vowel = []
for ing in 'aeiou':
    vowel.append(ing)
print(ing)
lst =[[]] * 4
lst[0].append(23)
def add(lst):
    lst += [3]
    return lst
print(add([1, 2, 3]))
lst, val = [], [[]]
lst = val + val + val
val.append(1)
print(lst)
lst = [[]] * 3
print([id(inner) for inner in lst])
lst = [[] for _ in range(3)]
print([id(inner) for inner in lst])
lst = []
lst.append([])
lst.append([])
lst.append([])
for k in lst:
    print(id(k))
for i, val in enumerate(lst):
    print((i, val), end = ' ')
def func(lst = []):
    lst.append(1)
    print(lst)
func([2])
func([3])
def func(lst = None):
    if not lst:
        lst = []
        lst.append(1)
        print(lst)
func()
x = []
func(lst = x)
func(lst = "")
func(lst = 0)
def func(lst = None):   
    if lst is None:        
        lst = []    
        lst.append(1)   
        print(lst) 
func()
lst = [0, 1, 2]
for idx, val in enumerate(lst):
    lst.pop(idx)
    print(lst)
lst = [1, 2, 3, 4, 5, 6, 7]
for idx, item in reversed(list(enumerate(lst))):
    if item % 2 == 0:
        lst.pop(idx)
print(lst)
lst = [0, 1, 2]
for idx, val in enumerate(lst):
    if idx == 20:
        break
    lst.insert(idx, 'a')
print(lst)
lst = [1, 2, 3, 4, 5, 6, 7]
for item in lst:    
    if item % 2 == 0:        
        item = 'even' 
print(lst)
lst = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(lst):  
    if item % 2 == 0:        
        lst[index] = 'even' 
print(lst)
lst = [0, 1, 2]
while lst:    
    print(lst[0])   
    lst.pop(0) 
print(lst)
lst, x = [0, 1, 2], 1
while len(lst) > x:    
    print(lst[0])   
    lst.pop(0) 
print(lst)
lst ,i = [1, 2, 3, 4, 5], 0
while i < len(lst):   
    if lst[i] % 2 == 0:       
        lst.pop(i)   
    else:
         i += 1
print(lst)
lst, tmp = [1,2,3,4,5], []
for item in lst:   
    if item % 2 != 0:       
        tmp.append(item)
lst = tmp 
print(lst)
lst = [1, 2, 3, 4, 5]
print([item for item in lst if item % 2 != 0])
print([x * 2 for x in lst])
print([x ** 2 for x in lst])
print([x for x in [1, 2, 3]])
print([i for i in range(11) if i % 2 == 0])
print([[j for j in range(3)] for i in range(3)])
print([character for character in 'Geeks 4 Geeks!'])

"""				"""
lst = [1, 2, 3, 4, 1, 2, 1, 3, 4]
print(lst.count(1))
import copy
lst = [[1, 2]]; tis = copy.copy(lst); tst = copy.deepcopy(lst)
print(lst is tis, lst[0] is tis[0])
print(lst is tst, lst[0] is tst[0])
lst = [1, 2, 3]
tis = lst[:]
print(tis, lst is tis)
head, *tail = [1, 2, 3, 4, 5] ; print(head, *tail)
lst = [1, 2, 3, 4, 5]
head, tail = lst[0], lst[1:] ;print(head, tail)
a, _ = 1, 2; print(a, _)
a, *_ = [1, 2, 3, 4, 5]; print(a, *_)
a, *_, b = [1, 2, 3, 4, 5]; print(a, b, *_)
a, _, b, _, c, *_ = [1, 2, 3, 4, 5, 6]; print(a, b, c)
listtuples = [(0, 10), (1, 15), (2, 8)]
print(min(listtuples))
print(min(listtuples, key = lambda x: x[0]))
print(min(listtuples, key = lambda x: x[1]))
print(sorted(listtuples, key = lambda x: x[0])) 
print(sorted(listtuples, key = lambda x: x[1]))

names = ['Fred', 'Wilma', 'Barney']
map_result = map(len, names)  
print("Using map:", list(map_result))  
from itertools import imap  
list_comprehension_result = [len(item) for item in names]
print("Using list comprehension:", list_comprehension_result)  
generator_expression_result = (len(item) for item in names)
print("Using generator expression:", list(generator_expression_result))  

import operator  
print(max(listtuples, key = operator.itemgetter(0)))
print(max(listtuples, key = operator.itemgetter(1)))
print(sorted(listtuples, key = operator.itemgetter(0), reverse = True))
print(sorted(listtuples, key = operator.itemgetter(1), reverse = True)) 
print(max([], default = 42))
print(max([], default = 0))

collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for item in collection:
    i1, i2, i3 = item[0], item[1], item[2]
    print(i1, i2, i3)
for item in collection:
    i1, i2, i3 = item
    print(i1, i2, i3)
for i1, i2, i3 in collection:
    print(i1, i2, i3)
    
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for i in lst:    
    print (i[:1], end = " ")
for idx, i in enumerate(lst):    
    print("%s has an index of %d" % (i, idx))
for i in range(2, 4):   
    print("lst at %d contains %s" % (i, lst[i]))
for s in lst[1::2]:    
    print(s)
    for i in range(1, len(lst), 2):
        print(lst[i])

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (lst[1], lst[0][0], lst[0][1])
a, b = [1, 2, 3, 7, 4, 5], [8, 9]
a.append(7); a.append(b); a.extend(b)
a.insert(0, 0); a.insert(2, 5); a.extend(range(3))
print(a.index(7), a.index(7, 8), a.pop(8), a.count(7))
a.pop(); a.reverse(); 
# a.sort(); a.sort(reverse = True)
ing = "Hello"; a.append(ing)
print(a, a + b)

import datetime
lst = [{'name' : 'John Cena', 'birthday' : datetime.date(1992, 9, 12), 'height' :  175},
    {'name' : 'Chuck Norris', 'birthday' : 
    datetime.date(1990, 8, 28), 'height' : 180},
    {'name' : 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'height': 185}]
lst.sort(key = lambda item: item['name'])
lst.sort(key = lambda item: item['birthday'])
lst.sort(key = lambda item: item['height'])
import datetime
lst = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'size': {'height': 175, 'weight': 100}}, 
    {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),'size' : {'height': 180, 'weight': 90}}, 
    {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'size': {'height': 185, 'weight': 110}}] 
lst.sort(key = lambda item: item['size']['height'])
print(lst)

from operator import itemgetter,attrgetter 
people = [{'name':'chandan','age':20,'salary':2000}, {'name':'chetan','age':18,'salary':5000}, {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age') 
by_salary = itemgetter('salary') 
people.sort(key = by_age)
people.sort(key = by_salary)
print(people)

lsttup = [(1,2), (3,4), (5,0)] 
lsttup.sort(key = itemgetter(1)) 
print(lsttup)

lst = ["blah"] * 3; lst.clear()
lst = [1, 3, 5] * 5
tis = list(range(10)) 
del tis[::2]; del tis[-1]; del tis[:]
print(lst, tis)

lst = [1, 2, 3, 4]
print(lst[-1], lst[-2], lst[-3], lst[len(lst)-1], lst[1:], lst[:3], lst[::2])
print(lst[::-1], lst[-1:0:-1], lst[5:8], lst[1:10], lst[::-1], lst[3:1:-1])
print(list(reversed(lst))[0:2])

data = 'chandan purohit 22 2000'
name, age, salary = slice(0,19), slice(19, 21), slice(22, None)
print(data[name], data[age], data[salary]) 
lst = []
for ch in 'Geeks 4 Geeks!': 
    lst.append(ch)
print(lst)
lst = []
if not lst: print("list is empty")
lst = ['foo', 'bar', 'baz']
for item in lst:    
    print(item)
for (index, item) in enumerate(lst):    
    print('The item in position {} is: {}'.format(index, item))
for i in range(0, len(lst)):    
    print(lst[i], end = " ")
for item in lst:    
    if item == 'foo':        
        del lst[0]    
    print(item, end = " ")
lst = ['test', 'twest', 'tweast', 'treast']
print('test' in lst, 'toast' in lst)
slst = set(lst);print('test' in slst)
lst, tis = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3', 'b4']
for a, b in zip(lst, tis):  
    print(a, b, end = " ")
print(len(list(zip(lst, tis))))
alist = [123, 'xyz', 'zara', 'abc'] 
alist.insert(3, [2009])
print("Final List :", alist)
import itertools
alist, blist, clist = ['a1', 'a2', 'a3'],  ['b1'], ['c1', 'c2', 'c3', 'c4'] 
for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c, end = " ")
print(len(['one', [2, 3], 'four']))
names = ["aixk", "duke", "edik", "tofp", "duke"] 
print(list(set(names)))
import collections
collections.OrderedDict.fromkeys(names).keys()
lst = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
print(lst[0][0][1], lst[1][1][2])
lst[0][0].append(11)
print(lst[0][0][2])
for row in lst:
    for col in row:       
        print(col, end = " ")
print([col for row in lst for col in row])
lst[1].insert(2, 15)
for row in range(len(lst)): 
    for col in range(len(lst[row])):       
        print(lst[row][col], end = " ")
print(lst[1][1:], lst)
lst = [None] * 10
lst = ['test'] * 10
lst=[{1}] * 10
print(lst)
lst[0].add(2)
print(lst)
print([{1} for _ in range(10)])

squares = [x * x for x in (1, 2, 3, 4)]
for x in (1, 2, 3, 4): squares.append(x * x)
print(squares)
print([s.upper() for s in "Hello World"])
print([w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']])
ing = "Beautiful is better than ugly"
print(["".join(sorted(word, key = lambda x: x.lower())) for word in ing.split()])
print([x if x in 'aeiou' else '*' for x in 'apple'])
def foo(i):    
    return i, i + 0.5
def generate_strings():
    for i in range(3):    
        for x in foo(i):   
            yield str(x)
print([ str(x) for i in range(3) for x in foo(i) ])
print(list(generate_strings()))
print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])
[print(x) for x in (1, 2, 3)]
from random import randrange 
print([randrange(1, 7) for _ in range(10)])
print([x for x in range(10) if x % 2 == 0])
"""            """
even_numbers = []
for x in range(10):   
    if x % 2 == 0:        
        even_numbers.append(x)
print(even_numbers)
print([x if x % 2 == 0 else None for x in range(10)])

data = [[1, 2], [3, 4], [5, 6]] 
print([element for lst in data for element in lst])
data = [[1, 2], [3, 4], [5, 6]] 
def func():
    output=[]
    for lst in data:         
        for element in lst:    
            output.append(element)      
    return output
data = [[1], [2, 3], [4, 5]] 
print([element for lst in data if len(lst) == 2 for element in lst if element != 5])
print([x**2 for x in range(10)])
for i in [x**2 for x in range(10)]:   
    print(i, end = " ")
print({x for x in range(5)})
print({x for x in range(1, 11) if x % 2 == 0})
ing = "When in the Course of human events it becomes necessary for one people..." 
print({ch.lower() for ch in ing if ch.isalpha()})
from functools import reduce
print(filter(lambda x: x % 2 == 0, range(10)))
print(map(lambda x: 2*x, range(10)))
print(reduce(lambda x,y: x+y, range(10)))
print([x for x in range(10) if x % 2 == 0])
print([2*x for x in range(10)])

print([x + y for x, y in [(1, 2), (3, 4), (5, 6)]])
print([x + y for x, y in zip([1, 3, 5], [2, 4, 6])])
for x, y in [(1,2), (3,4), (5,6)]:    
    print(x + y)
print([(x, y) for x, y in [(1, 2), (3, 4), (5, 6)]])
print(sum(1 for x in range(1000) if x % 2 == 0 and '9' in str(x)))
items = ["1", "2", "3", "4"] 
print([int(item) for item in items])
print(map(float, items))
print([x + y for x in [1, 2, 3] for y in [3, 4, 5]])
print([[x + y for x in [1, 2, 3]] for y in [3, 4, 5]])
lst = [] 
for y in [3, 4, 5]:    
    temp = []   
    for x in [1, 2, 3]:      
        temp.append(x + y)    
    lst.append(temp)
print(lst)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([[row[i] for row in matrix] for i in range(len(matrix))])
print([[[i + j + k for k in 'cd'] for j in 'ab'] for i in '12'])

list_1 = [1, 2, 3 , 4] 
list_2 = ['a', 'b', 'c', 'd'] 
list_3 = ['6', '7', '8', '9']
print([(i, j) for i, j in zip(list_1, list_2)])
print([(i, j, k) for i, j, k in zip(list_1, list_2, list_3)])
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[::2], lst[::3], lst[2 : 4], lst[2:], lst[:4])

a = [1, 2, 3, 4, 5]
b = a[::-1]
a.reverse()
if a == b:   
    print(True) 
print(b)
def shift(lst, pos):
    pos %= len(lst)
    pos *= -1
    shifted = lst[pos:] + lst[:pos]
    return shifted
lst = [1, 2, 3, 4, 5]
shift(lst, -7)
shift(lst, 5)
shift(lst, 3)
lst = [3, -4, -2, 5, 1, 7]
print(sorted(lst, key = lambda x: abs(x)))
print(list(filter(lambda x: x > 0, lst)))
print(list(map(lambda x: abs(x), lst)))
def append(val, to = []):
    to.append(val) 
    return to
append(1)
append(3, [])
def append(elem, to = None):
    if to is None:      
        to = []
    to.append(elem)    
    return to
def foo(x):
    x[0] = 9
    print(x)
y = [4, 5, 6] 
foo(y)    
print(y)
def foo(x): 
    x[0] = 9          
    x = [1, 2, 3]  
    x[2] = 8     
y = [4, 5, 6]  
foo(y)          
x = [3, 1, 9]
y = x 
x.append(5); x.sort()      
x = x + [4]   
x += [6]       
x = sorted(x); print(x)
ing = "abcdef"
print(ing[-1], ing[:], ing[::], ing[3:], ing[:4], ing[2:4], ing[::2], ing[1:4:2], ing[5:None:-1], ing[::-1], ing[5:0:-1])
lst = [1, 2, 3, 4, 5, 7, 8, 9]
lst[1:3] = [6]; lst[4 : 6] = [0, 1]
print(lst)
lst[:] = [4, 5, 6]
print(lst) 
lst[:] = [4, 5, 6]
print(lst) 
lst[-2:] = [4, 5, 6] 
print(lst) 
lst = ['a', 'b', 'c'] 
tis = lst[:]
lst.append('d') 
print(lst, tis)   

lst = ['zero', 'one', 'two'] 
print("2nd element is: {0[2]}".format(lst))
lst = [12,45,78]
print(map('the number is {}'.format, lst))
def func(lst, incr): 
    result = lst[0] 
    lst[0] += incr 
    return result
lst = [0]
print(f'{func(lst, 2)} {func(lst, 3)}')
print(f'{func(lst, 2)} {func(lst, 3)}')
data = ["a", "bbbbbbb", "ccc"] 
maxi = max(map(len, data)) 
for i in data:
    print('{:>{}}'.format(i, maxi))

import time
def for_loop(n): 
    result = [] 
    for i in range(n): 
        result.append(i**2) 
    return result
def list_comprehension(n): 
    return [i**2 for i in range(n)] 
begin = time.time() 
for_loop(10 ** 6) 
end = time.time() 
print('Time taken for_loop:', round(end - begin, 2)) 
begin = time.time() 
list_comprehension(10 ** 6) 
end = time.time() 
print('Time taken for list_comprehension:', round(end - begin, 2))

matrix = [] 
for i in range(3): 
    matrix.append([]) 
    for j in range(5): 
        matrix[i].append(j) 
print(matrix)
print([[j for j in range(5)] for i in range(3)])
numbers = [] 
for i in range(1, 6): 
    numbers.append(i*10) 
print(numbers)
print([i * 10 for i in range(1, 6)])
print(list(map(lambda i: i * 10, [i for i in range(1, 6)])))
print(["Even number" if i % 2 == 0  else "Odd number" for i in range(8)])
print([num for num in range(100) if num % 5 == 0 if num % 10 == 0])
print([n**2 for n in range(1, 11)])
matrix = [[10, 20, 30], [40, 50, 60],  [70, 80, 90]]
print([[i[j] for i in matrix] for j in range(len(matrix[0]))])
ing = 'Geeks4Geeks'
print(list(map(lambda i: chr(ord(i) ^ 32), ing)))
print([ing[::-1] for ing in ('Geeks', 'for', 'Geeks')])
names, ages = ["G", "G", "g"], [25, 30, 35] 
print([(name, age) for name, age in zip(names, ages)])

def digitSum(n): 
    dsum = 0
    for ele in str(n): 
        dsum += int(ele) 
    return dsum 
lst = [367, 111, 562, 945, 6726, 873] 
print([digitSum(i) for i in lst if i & 1])
print([l ** 3 for l in lst])
words = ["apple", "banana", "cherry", "orange"] 
print([len(word) for word in words])

a = 1
if a in (1, 2, 3):
    print(f"{a} is in the tuple (1, 2, 3)")
print(list(filter(lambda x : x.isalpha(), 'a1b2c3')))
lem = filter(lambda x : x.isalpha(), 'a1b2c3')
print(''.join(lem))
print(list(map(lambda x : x * x, [1, 2, 3])))
print(list(map(lambda x, y, z : (x, y, z), [1, 2, 3], [1, 2], [1, 2, 3, 4])))
print(list(zip([0, 1, 2], [3, 4, 5])))
print(list(map(lambda x : x[0] + x[1], zip(range(5), range(5)))))
print(list(map(lambda x : x[0] + x[1], zip(range(5), range(5)))))
print(list(range(1, 10)))
print(map(str, [1, 2, 3, 4, 5]), list(map(str, [1, 2, 3, 4, 5])))
lst = [1, 2, 3, 4, 5]
lst2 = lst
print(f"in: {2 in lst}\nnot in: {7 not in lst}\nis: {lst is lst2}\nis not: {lst is not lst2}")

import operator
print(operator.contains([1, 2, 3, 4, 5], 2))
print(operator.contains("Hello World", 'O'))
print(operator.contains({1, 2, 3, 4, 5}, 6))
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))
print(operator.contains((1, 2, 3, 4, 5), 9))
from functools import reduce
lst = [5, 8, 10, 20, 50, 100]
print(reduce((lambda x, y : x + y), lst))
print(reduce(lambda x, y : x if x > y else y , lst))
print(list(accumulate(lambda x, y : x + y, lst)))
"""                """
import operator
import itertools
print(reduce(operator.add, lst))
print(reduce(operator.mul, lst))
print(reduce(operator.add, ["Here", "I", " Am"]))
print(list(itertools.accumulate(lst, lambda x, y: x + y)))
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
result = reduce(lambda x, y: x * y, [1, 2, 3, 4], initializer=2)
print(result)
"""                """
tup = (2, 1, 0, 0, 0, 2, 2, 2)
print(reduce(lambda x , y : x + y, tup, 6))

import datetime
today = datetime.datetime.today()
print(f"{today :%B %d %Y} ")
print('''Geeks'for'Geeks''')
line = ord('\n')
print(f"newline: {line} ")
print(f"{{Double Braces}} ")

dic = {'id' : 10, 'Name' : 'molla'}
print(f"id: {dic['id']} name: {dic['Name']} ")
num = 3.14167
formatted = f"{num :.2f} "
print(formatted)
name, age = "Aslam", 22
sentence = "name {} age {}".format(name, age)
print(sentence)

x, y = 5, 10
print(["Less than", "Equal", " Greater than"][(x > y) - (x < y) + 1])
from itertools import filterfalse
names = ['Fred', 'Wilma', 'Barney']
def longName(name):
    return len(name) > 5
print(filter(longName, names), list(filter(longName, names)))
print(list(filterfalse(longName, names)))
print([name for name in names if len(name) > 5])
print(list(filter(None, [1, 0, 2, [], '', 'a'])))
from itertools import filterfalse
print(list(filterfalse(None, [1, 0, 2, [], '', 'a'])))
"""                     """
alist = ['wolf', 'sheep', 'duck'] 
print(list(filter(lambda x : x.startswith('d'), alist)))
from operator import methodcaller
print(list(filter(methodcaller('startswith', 'd'), alist)))
"""				"""
