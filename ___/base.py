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


