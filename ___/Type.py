#keyword
import keyword
print(keyword.kwlist)
#raise
tmp = "am ironman"
if tmp != "am":
    raise TypeError("Both the string are different")
    
frset = frozenset({"A", "B", "C"})
bit = bytearray(4)
mem = memoryview(bytes(6))
print(f"frset: {frset}\nbitarr: {bit}\nmemview: {mem} ")
#comparison
comp = 6
print(f"6 == 6: {comp == 6}\n6 != 6: {comp != 6}\n6 >= 6: {comp >= 6}\n6 <= 6: {comp <= 6}\n7 == 6: {(comp + 1) == 6}")
# chaining comparison operators
a = 5
print("1 < a < 10: ",1 < a < 10)
print("10 > a <= 9: ",10 > a <= 9)
print("5 != a > 4: ",5 != a > 4)
print("a < 10 < a*10 == 50: ",a < 10 < a*10 == 50)
#logical
a, b, c = 7, 9, True
print((a > 4) and (b < 10) and c)
print((a > 4) or (b < 10))
print(not(c))
#Bitwise
print(f"7 | 9: {a | b}\n7 & 9: {a & b}\n7 ^ 9: {a ^ b}\n~7: {~a}\n7 << 2: {a << 2}")
#identity operator
print(f"7 is 9: {a is b}\n7 is not 9: {a is not b} ")
ing = "ibrahim"
print("m" in ing, "x" not in ing)
c, d = 5, 5
e = 5
print(id(c) == id(e), id(d) == id(c))
#membership operator
lst = [1, 2, 3, 4, 5]
lst2 = lst
print(f"in: {2 in lst}\nnot in: {7 not in lst}\nis: {lst is lst2}\nis not: {lst is not lst2}")

# Assign value
a, b, _ = 1, 2, 3
c = d = e = 1
print(f"values are:",a, b, _, c, d, e)
#Convert string
a = "Hello"
print(type(a), list[a], tuple(a), set(a), a[0 : 4])
#datetime
import datetime
today = datetime.datetime.now()
print(repr(today), str(today))

from math import *
from random import *
from time import sleep

floorVal = floor(3.900)
ceilVal = ceil(4.0001)
print(floorVal, ceilVal)
print(random())
print(randint(1, 100))
sleep(4)
print(choice(['A', 'B', 'C', 'D', 'E']))

#try Except
try:
    x = 45 / 1
    print(x)
except:
    print("Error heppend")
finally:
    print("Done")
#conversion
x, y = 10, 20.5
print(type(x), type(y))
print(x + y)
print("sum is:",int("10") + int("10"))
first = input("Enter first:")
sec = input("Enter second: ")
print(str(first), float(sec))
print(0o123, 0O123) #octal to decimal
print(0b101, 0B101) #Binary to decimal
print(0x87, 0X87) #Hexa to decimal
print(type(0o123), type(0b101), type(0x87))

length = len("ibrahim")
print("name has " + str(length) + " character")

#decorator
def double_dacker():
    print("dacker")
    def inner():
        print("inner")
        return inner
    return 3000
print(double_dacker())
print(double_dacker()())
double_dacker()()

def something(work):
    print("start")
   # print(work())
    work()
    print("End")
def coding():
    print("coded")
# something(2)
something(coding)

def tim(func):
    def outer():
        print("started")
        print(func)
        print("outer")
    return outer
def get():
    print("Factorial starting")
tim(get)()

import time
def timer(func):
    def outer(*args, **kargs):
        start = time.time()
        print("starting")
        res = func(*args, **kargs)
        print("Ended")
        end = time.time()
        print({end - start})
        return res
    return outer
import math
@timer
def fact(n):
    print("start")
    res = math.factorial(n)
    print(res)
timer(fact(n = 5))
@timer
def out():
    print("Going")
out()
import math as mt
print(mt.factorial(5))

age, name, double, single = 45, "Hasan", 3.90, True
print(age, name, double, single)
print(type(age), type(name), type(double), type(single))
MyClass = type('MyClass', (object,), {'attr': 5})
print(type(MyClass))
print(age + double, age * double)
print(f"Name: {name}\nage: {age}\nmoney: {double}\nsingle: {single} ")

first = input("Enter first: ")
sec = input("Enter second: ")
intFirst = int(first)
intSec = int(sec)
#relational
print(f"first != second :{intFirst != intSec}\nfirst >= second :{intFirst >= intSec}\nfirst <= second :{intFirst <= intSec}\nfirst == second :{intFirst == intSec}")
#Assing
a, boss = 23, True
a += 32 # a *= 5 # a -= 32 # a /= 2
print(a)

#random
from random import *
#import random
#x = random.randint(a, b)
x = randint(1, 7) #a <= x <= b
x = randrange(1, 7) #a <= x < b
x = random() #x < 1
x = uniform(1, 3) #a < x <= b(return float value)
l = [2, 8, 5, 1, 9]
x = choice(l)
print(l)
shuffle(l)
print(x)
#round
print(f"round(2.5222, 2): {round(2.52222, 2)}\nround(2.555): {round(2.555)}\nround(2.5): {round(2.5)}\nround(674, -1): {round(674, -1)}\nround(675, -1): {round(675, -1)}\nround(674, -2): {round(674, -2)}\nround(675, -2): {round(675, -2)}" )
print(f"round(675, -3): {round(675, -3)}\nround(-8/3, 2): {round(-8/3, 2)}\nround(-1.5, 2): {round(-1.5, 2)}\nround(675.678, -1): {round(675.678, -1)}\nround(6.777, 2): {round(6.777, 2)}\nround(6.777): {round(6.777)}\n " )

#contains
import operator
print(operator.contains([1, 2, 3, 4, 5], 2))
print(operator.contains("Hello World", 'O'))
print(operator.contains({1, 2, 3, 4, 5}, 6))
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))
print(operator.contains((1, 2, 3, 4, 5), 9))
"""				"""
a, b = True, False
print("type of bool is: ", type(a), type(b))
x, y = 10, 5
print("bool of integer is: ", bool(x == y))
a, b, c, d= None, (), {}, 0.0
#return false as it's none
print("type of none is: ", bool(a), bool(b), bool(c), bool(d))
e, f, g = 10, 20, -39
print("type equivalenze is: ", e == f, bool(g))

print(2 ** 3, 2 ** -3, (-2) ** 0.5)
num = -8
num = 6 * 6.9
num = 2.7 + 9.8
num = (1 + 5j) + (3 + 2j)
num = (1 + 5j) - (3 + 2j)
num = (1 + 5j) * (3 + 2j)
num = (1 + 5j) / (3 + 2j)
num = 4.8
num = '3'
print(int(num), type(int(num)))
num = 6.7
print(complex(num))
print(num, type(num))
num = 7 * 3.0
print(type(num))
print(pow(3, 4, 17)) # 3 ** 4 % 17
x = 2 ** 100
cube = x ** 3
root = cube ** (1.0 / 3)
print(root)

import decimal
print(decimal.Decimal('1.1') + decimal.Decimal('4.9'))
"""						"""
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
"""                """
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
"""					"""
#Boolean logic
print(1 and 2, 1 or 2, None or 1, 0 or [])
print(1 and "Hello", "" and "Hello", )
def printf():
    print("Here i am")
printf() and 0

x, y = 5, 10
print(["Less than", "Equal", " Greater than"][(x > y) - (x < y) + 1])

import datetime
aDate = None 
if not aDate:
    aDate = datetime.date.today()
print("Assigned date:", aDate)
#filter
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
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
def findSmaller(tup):
    print('Check {0}, {1}$'.format(*tup)) 
    return tup[1] < 100  
result = next(filter(findSmaller, car_shop), None)
print("Result:", result)
generator = (car for car in car_shop if not car[1] < 100) 
next(generator)
"""                """
alist = ['wolf', 'sheep', 'duck'] 
print(list(filter(lambda x : x.startswith('d'), alist)))
from operator import methodcaller
print(list(filter(methodcaller('startswith', 'd'), alist)))
"""				"""
a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a / b, a / c, d / b, b / a, d / e)
print(a / (b * 1.0), 1.0 * a / b, a / b * 1.0, float(a) / b, a / float(b))
print(3 * ('ab'), 3 * ('a', 'b'))
print((5 + 2), (5 + 0.2), 2 + (2 + 2j), (0.5 + 0.5), 0.2 + (2 + 2j), (3 + 2j) + (6 + 2j))
"""				"""
foo, bar, baz = 1, 'baz', 3.1416
print(str(foo) + " " + bar + " " + str(baz))
print("4" + "5", [4] + [5])
print("Aa", "Bb", "Cc", sep = ",")
print("<a ", end=''); print("class = 'jidn'" if 1 else "", end=''); print("/>")
print("paragraph1", end="\n\n"); print("paragraph2")
