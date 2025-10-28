from __future__ import unicode_literals
print(repr("HI"))
print(help("modules"), help("random"))
begin, *tail = "HELLO"; print(*tail, begin)
x, ing = 1, "flow"; print(id(x), id(ing))
x += 2; ing += "over"; print(id(x), id(ing))
print(-8 == (-7 - 1), -3 == (-2 - 1))
a, b, c = 1, 2, 3
if a == 3 or b == 3 or c == 3:    print("TRUE")
if any([a == 3, b == 3, c == 3]):    print("TRUE")
if 3 in (a, b, c):    print("3 is present")
if any(x == 3 for x in (a, b, c)):    print("3 is found")
print((7).bit_length(), (7.2).as_integer_ratio())
print(2 ** 3, (-(2 ** 3)), type(2 ** 1024))
print(len("jenny"))
lst = ["jenny", 7]; print(len(lst))
dic = {1 : "A", 2 : "B", 3 : " C"}; print(len(dic))
line = ord('\n'); print(f"newline: {line} ", f"{{Double Braces}} ")
print('''Molla'4'Now''')
print(len([1, 2]) > len('foo'), len((1, 2)) > len([1, 2]), 100 < 200, 'abc' < 'xyz', (1, 'x') < (2, 'y'))
print(round(1.5), round(.5), round(-.5), round(-1.5), round(4.8))
print(range(1, 10), range(1, 10)[2 : 8], range(1, 10).count(5), range(1, 10).index(7))
from math import *
x, y = 1.55, -1.55
print(pi, sin(1), sqrt(2), ceil(2.7))   
print(round(x), round(y), round(x + 1, round(y + 1)), floor(x), ceil(x), trunc(x))
import math as mt
print(mt.hypot(2, 4), mt.radians(45), mt.degrees(mt.asin(1)), mt.sin(mt.pi / 2))
print(mt.sin(mt.radians(90)), mt.asin(1), mt.asin(1) / mt.pi, mt.cos(mt.pi / 2))
print(isinstance(range(1, 10), range))
g = (i for i in range(0, 3)); print(next(g), next(g), next(g))
i = 0; print([i for i in range(3)])

from time import sleep
import math
def fact(num):
    sleep(0.0001)
    res = 1
    while num >= 1:
        res *= num;    num -= 1
    return res
    #return math.factorial(5)
print(fact(5))
cnt = 3
for i in reversed(range(cnt + 1)):
    if i > 0:
        print(i, end = ' ', flush = True); sleep(0.5)
    else:    print("starting")
print(10, 20, 30, sep = '-')
a, b = 10, 20
def xyz():
    return a, b
a, b = xyz(); print(a, b)
import keyword as kw
print(kw.kwlist)
tmp = "am ironman"
try:
    if tmp != "am":    raise TypeError("Both are Diffrent")
except TypeError as e:    print("Caught an error:",e)
def divide(x, y):
    try:    print(x // y)
    except ZeroDivisionError:    print("Dividing by zero")
    #except Exception as e:    
        #print(f"An error occurred: {type(e).__name__} -> {e}")
divide(3, 2); divide(3, 0)
#divide(3, "Aa")
def fork(a, b):
    try:    c = (a + b) // (a - b)
    except ZeroDivisionError:    print ("a/b result in 0")
    else:    print (c)
fork(2.0, 3.0); fork(3.0, 3.0)
print(frozenset({"A", "B", "C"}), bytearray(4), memoryview(bytes(6)))
print(6 == 6, 6 != 6, 6 >= 6, 6 <= 6, 7 == 6, (6 + 1) == 7)
x = 5
print(1 < x < 10, 10 > x <= 9, 5 != x > 4, x < 10 < x * 10 == 50)
a, b, c = 7, 9, True
print((a > 4) and (b < 10) and c, (a > 4) or (b < 10), not(c))
print(a | b, a & b, a ^ b, ~a, a << 2, a >> 1)
print(a is b, a is not b)
#~n = -|n + 1|, ~-n = |n - 1|
a, b = 10, -20; print(~a, ~b)
c, d = 0, 1; print(c ^ d, c & d, bin(c | d), d << 5, bin(100 >> 2))
a = 0b001; print(a); a &= 0b010; print(a)
a |= 0b010; print(a); a <<= 2; print(a)
a >>= 2; print(a); a ^= 0b011; print(a)
if 1 > -1 < 2 > 0.5 < 100 != 24:    print("Yes")
else:    print("No")
print("alpha" < "beta", '12' != '1', '12' == 12)

ing = "ibrahim"; print("m" in ing, "x" not in ing)
print(type(ing), list[ing], tuple(ing), set(ing), ing[0 : 4])
c, d = 5, 5
e = 5; print(id(c) == id(e), id(d) == id(e))
print(round(2.52222, 2), round(2.555), round(2.5), round(674, -1), round(675, -1), round(674, -2), round(675, -2))
print(round(675, -3), round(-8/3, 2), round(-1.5, 2), round(675.678, -1), round(6.777, 2), round(6.777))
print(round(1.3), round(1.33, 1), round(2.675, 2))
a, b, _ = 4, 5, 6
c = d = e = 3; print(a, b, _, c, d, e)
a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a / b, a / c, d / b, b / a, d / e)
print(a / (b * 1.0), 1.0 * a / b, a / b * 1.0, float(a) / b, a / float(b))
print(3 * ('ab'), 3 * ('a', 'b'))
print(5 + 0.2, 2 + (2 + 2j), 0.2 + (2 + 2j), (3 + 2j) + (6 + 2j))
print(str(1) + " " + str(3.1416), "4" + "5", [4] + [5])
print("Aa", "Bb", "Cc", sep = " - ")
print("<a ", end = ''); print("class = 'jidn'" if 1 else "", end = ''); print("/>")
print("MOLLA", end = "\t\t"); print(" VAI")
a = 5; print(eval("5 + 3 * a"))
a = b = c = 1
print(compile('a * b + c', '<string>', 'eval'))
print(compile('a * b + c', '<string>', 'single'))
print(compile('a * b + c', '<string>', 'exec'))
dic = {'a' : 7, 'b' : 6}; print(eval('a * b', dic))
import datetime as dt
day = dt.datetime.now(); print(repr(day), str(day))
now = None
if not now:    now = dt.date.today()
print(now)
from math import *
from random import *
from time import sleep
print(floor(3.99), ceil(4.0001))
print(random(), randint(1, 100))
sleep(1)
print(choice(['A', 'B', 'C', 'D', 'E']))
import random as rnd
print(rnd.randint(1, 7)) #a <= x <= b
print(rnd.randrange(1, 7)) # a <= x < b
print(rnd.random()) # 1 < x
print(rnd.uniform(1, 3)) # a < x <= b
x = [2, 8, 5, 1, 9]; print(rnd.choice(x))
rnd.shuffle(x); print(rnd.choice(x))
import random as rnd
print(rnd.randint(1, 10), rnd.random(), rnd.random() * 100)
print(str(rnd.randint(0, 12)), rnd.randrange(10, 20, 3)); rnd.seed(5)
print(rnd.randrange(0, 10), rnd.randrange(1, 10))
import inspect as ins
print(ins.getsource(rnd.randrange), ins.getdoc(rnd.randrange), ins.getmodule(rnd.randrange))

state = rnd.getstate(); rnd.setstate(state)
print(state, end = " ")
rnd.seed(None); rnd.seed()
prob = 0.3
if rnd.random() < prob:    print("Decision with probability 0.3")
else:    print("Decision with probability 0.7")
    
import decimal as dc
print(dc.Decimal('1.1') + dc.Decimal('4.9'))
try:
    x = 45 / 1; print(x)
except:    print("Error heppend")
finally:    print("Done")
print(int.__add__(7, 8), str.__add__("2", "3"))
x, y = 10, 25.50; print(type(x), type(y), x + y)
x += 32; print(x); x *= 5; print(x)
x -= 23; print(x); x /= 2; print(x)
print("sum is:",int("10") + int("10"))
first = input("Enter: "); sec = input("Enter: ")
print(str(first), float(sec)); 
front = int(first); back = int(sec)
print(front != back, front >= back, front <= back, front == back)
print(0o123, 0O123, 0b101, 0B101, 0x87, 0X87) #octal, binary, Hexa to decimal

length = len("ibrahim"); print("name has " + str(length) + " character")
#decorator
def double_dacker():
    print("dacker")
    def inner():
        print("inner")
    return inner
print(double_dacker(), double_dacker()())
double_dacker()() 
def func(work):
    print("inner"); work(); 
    print(work()); print(work)
    print("End")
def coding():    print("coded")
func(coding)  
def tim(func):
    def inner():
        print("started"); print(func)
        func(); print("End")
    return inner
def get():    print("starting")
tim(get()); tim(get)()
import time as ti
def timer(func):
    def inner(*args, **kargs):
        start = ti.time()
        print("initiate"); res = func(*args, **kargs)
        print("ended"); end = ti.time()
        print(f"Execution time: {end - start:.4f} sec"); return res
    return inner
@timer
def slow_function():
    ti.sleep(1.5);    print("running...")
slow_function()
import math as mt
@timer
def fact(n):
    print(mt.factorial(n))
timer(fact(n = 5))
@timer
def out():    print("Going")
out()   
dig, ing, point, cond = 45, "Hasan", 3.90, True; print(dig + point, dig * point)
print(dig, ing, point, cond, type(dig), type(ing), type(point), type(cond))
print(f"name: {ing}\t\tage: {dig}")
clas = type('mine', (object,),{'attr' : 5}); print(clas)
dig = input("Enter num: "); print(dig, type(dig), type(int(dig)))
ing = input("Enter name: "); print(ing, type(ing))
point = float(input("Enter floating: ")); print(point, type(point))

import datetime as dt
ing = input("Enter time(HH : MM : SS): ")
print(dt.datetime.strptime(ing, "%H:%M:%S"))
import datetime as dt
import time as tm
print(tm.time(), dt.date.fromtimestamp(454554))
once = dt.datetime(2010, 7, 1, 12, 0, 0) 
delta = dt.timedelta(days = 13, hours = 8,  minutes = 20)   
gen = (once + x * delta for x in range(5))
print('\n'.join(map(lambda d : d.strftime('%Y-%m-%d %H:%M:%S'), gen)))
print('North America: {dt:%m/%d/%Y}. ISO: {dt:%Y-%m-%d}.'.format(dt = dt.datetime.now()))

x, y, z = input("Enter values: ").split(); print(x, y, z)
print("first-{} second-{} third-{}".format(x, y, z))
x = list(map(int, input("Enter values: ").split())); print(x)
x, y, z = map(float, input("Enter values: ").split()); print(x * y *z, x + y + z)
x, y, z = [int(x) for x in input("Enter values: ").split()]; print(x, y, z)
print("first: {}\tsecond: {}\tthird: {}".format(x, y, z))
print([int(x) for x in input("Enter values: ").split()])
print([int(x) for x in input("Enter value: ").split(",")])
name, age = input("Enter name & age: ").split()
print(f"name: {name}\tage: {age}", end = '.')

a, b = True, False; print(type(a), type(b))
x, y = 10, 5; print(bool(x == y))
a, b, c, d, e, f, g = None, (), {}, 0.0, 10, 20, -39
print(bool(a), bool(b), bool(c), bool(d), bool (g), e == f)
print(2 ** 3, 2 ** -3, (-2) ** 0.5)
print(int(-8), type(int(-8)))
x = 6 * 6.9; print(int(x), type(int(x)))
x = 2.7 + 9.8; print(int(x), type(int(x)))
x = (1 + 5j) + (3 + 2j); print(x.real, x.imag, abs(x))
x = (1 + 5j) - (3 + 2j); print(x.real, x.imag, abs(x))
x = (1 + 5j) * (3 + 2j); print(x.real, x.imag, abs(x))
x = (1 + 5j) / (3 + 2j); print(x.real, x.imag, abs(x))
x = 4.8; print(int(x), type(int(x)), complex(x), )
x = '3'; print(int(x), type(int(x)))
x = 3 * 7.0; print(type(x), x)
print(pow(3, 4, 17)) # 3 ** 4 % 17
x = 2 ** 100; print((x ** 3) ** (1.0 / 3))
print(1 and 2, 1 or 2, None or 1, 0 or [])
print(1 and "Hello", "" and "Hello", )
def func():    print("Here i am")
res = func() and 0; print(res) 
shop = [('Toyota', 1000), ('rect tire', 80), ('Porsche', 5000)]
def findsmaller(tup):
    print('{0}, {1} £'.format(*tup))
    return tup[1] < 100
print(next(filter(findsmaller, shop), None))
print((car for car in shop if not car[1] < 100))
def sqrt(num):    print('{}'.format(num))
sqrt(4)
def or_(a, b):
    if a:    return a
    else:    return b
def and_(a, b):
    if not a:    return a
    else:    return b
print(or_(10, 15), and_(10, 15))
def T():    return True
def F():    return False
print(T() and F(), T() or F())
import math
print(math.acos(1), math.tan(math.pi/2), math.atan(math.inf), math.atan(float('inf')))
print(math.atan2(1, 2), math.atan2(-1, -2), math.atan2(1, 0), math.sinh(math.pi), math.asinh(1))
print(math.cosh(math.pi), math.acosh(1), math.tanh(math.pi), math.atanh(0.5), math.log(math.e))
print(math.log(1), math.log(100), math.log(1 + 1e-20), math.log1p(1e-20), math.log10(10))
print(math.log(100, 10), math.log(27, 3), math.log(1, 10), math.copysign(-2, 3)   )
print(math.copysign(3, -3), math.copysign(4, 14.2), math.copysign(1, -0.0), math.floor(-1.7))
print(abs(1 + 1j), complex(1), complex(imag = 1), complex(1, 1), complex(1 + 1j), abs(1 + 1j))
print(math.pow(2, 2), math.pow(2, -2), math.pow(-2, 5), math.e ** 2, math.exp(2), math.exp(10), math.exp(10).real)
print(math.e ** 1e-3 - 1, math.exp(1e-3) - 1, math.expm1(1e-3), math.e ** 1e-15 - 1, math.exp(1e-15) - 1, math.expm1(1e-15))
print(Decimal('6.25').sqrt(), math.sqrt(9), math.sqrt(11.11))
print(cmath.sqrt(4), cmath.sqrt(-4))
a, b = 1, 2
print(math.sinh(a), math.cosh(a), math.atan(math.pi))
print(math.hypot(a, b), math.degrees(a), math.radians(57.29577951308232))
num = cmath.sqrt(-1)
while num:
    print(num); break
import cmath
print(cmath.sqrt(-1), cmath.polar(1 + 1j), cmath.phase(1 + 1j), cmath.rect(math.sqrt(2), math.atan(1)))
print(cmath.phase(complex(-1.0, 0.0)), cmath.phase(complex(-1.0, -0.0)), cmath.log(1+1j), cmath.exp(1j * cmath.pi))
print(type(cmath.pi), cmath.isinf(complex(float('inf'), 0.0)), cmath.isnan(complex(0.0, float('nan'))), cmath.isinf(complex(0.0, math.inf)), cmath.isnan(complex(math.nan, 0.0)))
import cmath
z = cmath.rect(*cmath.polar(1 + 1j))  
x = 2 + 3j; print(abs(x))
print(cmath.isclose(z, 1 + 1j), cmath.phase(z), cmath.polar(z), cmath.rect(2, cmath.pi/2), cmath.exp(z), cmath.log(z))
print(cmath.log10(-100), cmath.sqrt(z), cmath.sin(z), cmath.cos(z), cmath.tan(z), cmath.asin(z), cmath.acos(z), cmath.atan(z))
print(cmath.sin(z)**2 + cmath.cos(z)**2,  cmath.sinh(z), cmath.cosh(z), cmath.tanh(z), cmath.asinh(z), cmath.acosh(z), cmath.atanh(z))
print(cmath.cosh(z)**2 - cmath.sin(z)**2,  cmath.cosh((0+1j)*z) - cmath.cos(z))
x.conjugate(); print(x)

import collections as col
print(col.Counter([1, 3, 5, 7, 9]))
print(col.Counter(['a', 'b', 'c', 'b']))
print(col.Counter(["Hi everyone", "where"]))
print(col.Counter('Here-I-am! where-are-u'.split()))
cnt = col.Counter({'a' : 1, 'b' : 2, 'c' : -3, 'd' : 0}); print(cnt)
cnt['d'] = 5; cnt.update({'b' : 5, 'c' : 7})
cnt.subtract({'a' : 1, 'b' : 1, 'c' : 1}); print(cnt)
print(sum(cnt.values()), cnt.elements(), cnt.keys())
print(cnt.values(), cnt.items())
cnt = col.Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(cnt, cnt.keys(), cnt.values(), cnt.items(), cnt["a"])
dic = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
print(col.Counter(dic.values()).most_common())
print(col.Counter(dic.values()).most_common(2))
from collections import deque
deq = deque('mollavai')
deq.append('a'); deq.pop(); deq.popleft();
deq.extend('jkl'); deq.extendleft('mnk'); deq.rotate(1)
deq.rotate(-1); print(deq, 'h' in deq)
print(deque.reverse(deq), list(deq), list(reversed(deq)))
for val in deq:    print(val.upper(), val.lower(), end = " ")
deq.clear()
deq, que = deque([1, 2, 3]), deque()
deq.popleft(); deq.appendleft(5);
que.append(2); que.extend([6, 7]); que.extendleft([-2, -1]);
que.popleft(); que.remove(7); que.reverse()
print(deq, que); 

def bfs(grid, root):
    dist = {}; dist[root] = 0
    q = deque([root])
    while q:
        curr = q.popleft()
        for adj in grid[curr]:
            if adj not in dist:
                dist[adj] = dist[curr] + 1
                q.append(adj)
    return dist
dic = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
print(bfs(dic, 1))
import operator as op
print(op.pow(4, 3), op.__pow__(4, 3))
x, y = 2, 6; print(x.__pow__(y), y.__rpow__(x), op.add(x, y), op.sub(x, y), op.truediv(x, y), op.floordiv(x, y))
from operator import *
print(add(1, 1), mul(2, 2), mul('a', 10), mul([3], 3))
import operator as op
print(op.contains([1, 2, 3, 4, 5], 2))
print(op.contains("Hello world", '0'))
print(op.contains({1, 2, 3, 4, 5}, 6))
print(op.contains([1, 2, 3, 4, 5], 9))
print(op.contains({1: "Geeks", 2: "for", 3: "geeks"}, 3))
from operator import truediv, floordiv
test = [ (10, 8), (10, -8), (-10, 8), (-10, -8), 
    (7.5, 2.5), (9, 3), (0, 5), (5, 2)]
for a, b in test:
    print(truediv(a, b), floordiv(a, b))
    assert truediv(a, b) == a / b
    assert floordiv(a, b) == a // b
import heapq as hq
print(hq.nlargest(5, range(10)), hq.nsmallest(5, range(10)))
num = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(hq.nlargest(4, num), hq.nsmallest(4, num))
hq.heapify(num); print(num)
hq.heappop(num); print(num)
info = [{'first': 'Abc', 'last': 'Doe', 'age': 30}, {'first': 'Def', 'last': 'Doe', 'age': 25},    
        {'first': 'Ghi', 'last': 'Doe', 'age': 10}, {'first': 'Jkl', 'last': 'Roe', 'age': 22},    
        {'first': 'Mno', 'last': 'Doe', 'age': 12}, {'first': 'Pqr', 'last': 'Roe', 'age': 45}]
print(hq.nlargest(2, info, key = lambda x : x['age']))
print(hq.nsmallest(2, info, key = lambda x : x['age']))

from queue import Queue
q = Queue()
for x in range(1, 10):
    dic = ('key', x); q.put(dic)
while(not q.empty()):    print(str(q.get())) 
import locale, functools as funto
print(sorted(['A', 'S', 'F', 'D'], key = funto.cmp_to_key(locale.strcoll)))

def func(a, b, c, x):    return 1000 * a + 100 * b + 10 * c + x
res = funto.partial(func, 1, 1, 1); print(res(5))
import itertools as it
for num in it.count():  
    if num > 20:    break
    print(num, end = " - ")
for num in it.count(start = 10, step = 4):
    print(num, end = "  ")
    if num > 30:    break
print()
print(list(it.combinations([1, 2, 3, 4, 5], 3)))
def func():
    n = 0
    while n < 20:    n += 1; yield n
for i in it.islice(func(), 3):    print(i, end = " - ")
def test(lst):
    group = it.groupby(lst, key = lambda x : x[1])
    for key, val in group:    print(key, list(val))
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)]; test(lst)
lst.sort(key = lambda x : x[1]); print(lst)
grp = it.groupby(lst, key = lambda x : x[1])
grplst = [(key, list(val)) for key, val in grp]
for key, val in grplst:    print(key, val)
for key, val in sorted(grplst):    print(key, val)
lst = [1, 2, 3]
print(list(it.permutations(lst)))
print(list(it.permutations(lst, 2)))
for i in it.repeat('over-and-over', 3):    print(i, end = " ")
print()
def IsEven(x):    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
print(list(it.dropwhile(IsEven, lst)))
print(list(it.takewhile(IsEven, lst)))
def customdrop(predicate, able):
    able = iter(able)
    for x in able:
        if not predicate(x):
            yield x; break
    yield from able
print(list(customdrop(IsEven, lst)))
print(list(it.takewhile(IsEven, lst)) + list(it.dropwhile(IsEven, lst)))
a, b = [i for i in range(5)], ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in it.zip_longest(a, b):
    x, y = i; print(x, y, end = "\n")
for i in it.zip_longest(a, b, fillvalue = "wash"):
    x, y = i; print(x, y, end = "\n")
def fetch():
    for i in range(50):    yield f"{i + 1}"
limit = 20
for data in it.islice(fetch(), limit):    print(data, end = " ")

dic = {
    "x": ["a", "b"], "y": [10, 20, 30]
}
key = dic.keys(); val = [dic[k] for k in key]
print([dict(zip(key, combination)) for combination in it.product(*val)])
import operator as op
print(list(it.accumulate([1, 2, 3, 4])))
print(list(it.accumulate([1, 2, 3, 4], func = op.mul)))
print(it.cycle('ABCDE'))
t = it.cycle('abc123')
print([next(t) for i in range(1, 10)])
for x, y in it.product(range(10), range(10)):    print(x, y, end = "\t")
print()
t = [range(10)] * 2
for x, y in it.product(*t):    print(x, y, end = "\t")
print()
x, y = [1, 2, 3, 4], ['a', 'b', 'c']; print(it.product(x, y))
for i in it.product(x, y):    print(i, end = " ")
print()
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['a', 'b', 'c'])
print(' '.join(it.chain(a, b)))
import functools as fun
import operator as op
x = fun.partial(raisepower, y = 3); print(x(5))
x = fun.partial(raisepower, y = 4); print(x(2))
print(fun.reduce(lambda x, y : x + y, [2, 4, 6, 8]))
print(fun.reduce(op.mul, [10, 5, -3]))
print(fun.reduce(op.and_, [False, True, True, True]))
print(fun.reduce(op.or_, [True, False, False, False]))
try:    print(raisepower(2, 6))
except notinlimit as e:    print(e)
def func(param):
    for val in param:
        print('{}'.format(val))
        if val == 1:    return
    return 'could\'nt find value'
print(func([5, 3, 2, 8, 9]))
def add(x, y):    return x + y
def mult(x, y):
    print(x * y); return x * y
seq = [1, 2, 3, 4, 5]
print(fun.reduce(add, seq), fun.reduce(add, seq, 10), fun.reduce(op.add, seq))
print(fun.reduce(mult, seq), fun.reduce(mult, seq, 10))
import itertools as it
def func(n):
    while True:
        yield n
        n += 1
#x = func(10)
x = it.count(1)
print(func(1), x)
drei = (i * 2 for i in x); print(list(it.islice(drei, 10)))
x = it.count(1)
tre = (i for i in x if i % 3 == 0); print(list(it.islice(tre, 10)))
x = it.count(1)
tmp = (i for i in x if i % 5 == 0)
print([next(tmp) for _ in range(3)])

vier = (i * 4 for i in func(1))
funf = list(it.islice(vier, 5)); print(funf)
print(next(x), next(drei), next(vier))
for idx, val in enumerate(drei):
    print(val, end = " ")
    if idx == 9:    break
def fib():
    a, b = 1, 1
    while True:
        yield a; a, b = b, a + b
print(list(it.islice(fib(), 10)))
def nth(n):    return next(it.islice(fib(), n - 1, n))
print(nth(99))

import hashlib as hb
m = hb.md5(); m.update('Nobody inspects'.encode())
print(m.digest(), m.hexdigest(), m.digest_size, m.block_size)
m.update('spammish repitition'.encode())
print(m.digest(), m.hexdigest(), m.digest_size, m.block_size)
print(hb.md5("Nobody inspects".encode()).hexdigest())
h = hb.new('ripemd160')
h.update("Nobody inspects the spammish repetition".encode()); print(h.hexdigest())

import threading as th
import multiprocessing as mp
def func():    print("Hello")
t = th.Thread(target = func)
t.start();    t.join()
import time
class nap(th.Thread):
    def run(self):    
        time.sleep(2)
        print("ciao")
if __name__ == "__main__":
    t = nap()
    t.start(); t.join()
    
def func(i):    return i * i
def other(m, i):    return m + i
def task():
    for j in range(100):    res = 0
    for i in range(1000):    res = other(res, func(i))
start = time.time();    task()
print(time.time() - start)
start = time.time()
#threads = [th.Thread(target = task) for i in range(4)]
threads = [mp.Process(target = task) for i in range(4)]
for t in threads:    t.start()
for t in threads:    t.join()
print(time.time() - start)
def countdown(n):
    while n > 0:    n -= 1
def runthread():
    COUNT = 10000000
    t1 = th.Thread(target = countdown, args = (COUNT // 2,))
    t2 = th.Thread(target = countdown, args = (COUNT // 2,))
    start = time.time()
    t1.start(); t2.start(); t1.join(), t2.join()
    print(f"{time.time() - start} seconds")
runthread()
import math
def fact(n):    print(math.factorial(n))
if __name__ == '__main__':
    num = 60
    p = mp.Process(target = fact, args = (num,))
    p.start(); p.join()
import pprint
obj, lock = {}, th.Lock()
def objify(key, val):
    print(f"[{th.current_thread().name}] Obj has {len(obj)} values")
    with lock:    obj[key] = val
    print(f"[{th.current_thread().name}] Obj now has {len(obj)} values")
ts = [th.Thread(target = objify, args = (str(n), n)) for n in range(4)]
for t in ts:    t.start()
pprint.pprint(obj)
for t in ts:    t.join()

"""
import os
def task():
    print("Pid is %s, thread id is %s" % (os.getpid(), th.current_thread().name))
def process():    print("Pid is %s" % (os.getpid(),))
threads = [th.Thread(target = process) for i in range(4)]
processes = [mp.Process(target = process) for _ in range(4)]
for t in threads:    t.start()
for t in threads:    t.join()
for p in processes:   p.start() 
for p in processes:   p.join()
import sys, codecs
print(sys.stdout.write('Hello World'))
print(sys.stdout.buffer.write(b'\\xf0\\x9f\\x90\\x8d\\n'))
print(codecs.stdout('1deadbeef4', 'hex'))
print(codecs.encode(b'\x1d\xea\xdb\xee\xf4', 'hex'))
print(codecs.encode(b'\x1d\xea\xdb\xee\xff', 'hex').decode('ascii'))
"""
import bisect as bis
import timeit as tim
def sortedIdx(seq, val):
    i = bis.bisect_left(seq, val)
    if i != len(seq) and seq[i] == val:    return i
    raise ValueError(f"{val} not found")
lst = [i for i in range(1, 100000, 3)]
print(sortedIdx(lst, 97285))
try:    print(sortedIdx(lst, 4))  
except ValueError as e:    print(e)
print(tim.timeit(lambda: sortedIdx(lst, 97285), number = 10000))
print(tim.timeit(lambda: lst.index(97285), number = 10000))
print(tim.timeit(lambda: sortedIdx(lst, 4), number = 10000))
try:    print(tim.timeit(lambda: lst.index(4), number = 10000))
except ValueError:    print("ValueError")
import unicodedata as udata
print([udata.name(char) for char in "ê"])
print([udata.name(char) for char in "e"])
print(udata.normalize("NFKD","ê") == udata.normalize("NFKD", "e"))
def caselessNormalize(text):    return udata.normalize("NFKD", text.casefold())
def caselessEqual(left, right):    return caselessNormalize(left) == caselessNormalize(right)
pairs = [
    ("Straße", "STRASSE"), ("café", "cafe"),   ("Êcole", "ecole"), 
    ("Hello", "hello"), ("𝐀𝐛𝐜", "Abc"), ("ﬁ", "fi")]
for left, right in pairs:
    print(f"Comparing '{left}' vs '{right}': {caselessEqual(left, right)}")

import typing as typ
point = typ.NamedTuple('point', [('x', int), ('y', int)])
p = point(3, 4); print(p.x, p.y)
x, y = p; print(x, y, p)
T = typ.TypeVar("T")
def getval(val: typ.Sequence[T], default: typ.Optional[T] = None) -> T:
    if val:    return val[0]
    if default is not None:    return default
    raise ValueError("Sequence is empty and no default value provided")
lst = [1, 2, 3]
strlst = ["apple", "banana", "cherry"]
empty_list = []
print(getval(lst), getval(strlst))  
print(getval(empty_list, default = "No elements"))  
"""            ARRAY            """
import array as arr
#from array import array
x = arr.array('d', [2.1, 3.4, 5.9, 7.8])
for i in range(4):    print(x[i], end = " ")
print("\r")
x = arr.array('i', [5, 9, 4, 7])
for i in range(0, 4):    print(x[i], end = " ")
x.insert(1, 9); x.append(10);print(x.pop(1))
for i in x:    print(x.pop(), end = " ")
if 2 in x:    x.remove(2)
for i in x:    print(x.pop(), end = " ")
print("\r")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = arr.array('i', x)
for i in l:    print(i, end = " ")
print(x[3 : 8], x[:], x.index(5), x.index(7))

x = arr.array('i', [9, 8, 7, 6, 5, 4])
x[2] = 2; x[4] = 6; x.extend([12, 13, 14]); x.reverse()
print(x.count(6), *x, x.tolist())
x.remove(4) #del first occurance
for i in x:    print(i, end = " ")
print("\r")
y = arr.array('i', [7, 8, 9]); x.extend(y)
c = [11, 12, 13]; x.fromlist(c)
print(x.buffer_info, x[0], x.index(9))

