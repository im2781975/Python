from __future__ import unicode_literals 
print(repr("hi"))
begin, *tail = "Hello"
print(begin, tail)
a, ing = 1, "stack"
print(id(a), id(ing))
print(-8 == (-7 - 1))
print(-3 == (-2 - 1))
print((255 + 1) == (255 + 1))
a, b, c = 1, 2, 3
if a == 3 or b == 3 or c == 3:
    print("True")
if any([a == 3, b == 3, c == 3]):
    print("Yes")
if 3 in (a, b, c):
    print("3 is present")
if any(x == 3 for x in (a, b, c)):
    print("3 is found")
if a in (1, 2, 3):
    print(f"{a} is in the tuple (1, 2, 3)")
print(7.bit_length())
print(7.2.as_integer_ratio())
a += 2
ing += "Overflow"
print(id(a), id(ing))
print(2 ** 3, (- (2 ** 3)), type(2 ** 1024))
print(len([1, 2]) > len('foo'), len((1, 2)) > len([1, 2]))
print((100 < 200), ('xyz' < 'abc'), (1, 'x') < (2, 'y'))
print(round(1.5), round(0.5), round(-0.5), round(-1.5), round(4.8))
print(list(filter(lambda x : x.isalpha(), 'a1b2c3')))
lem = filter(lambda x : x.isalpha(), 'a1b2c3')
print(''.join(lem))
print(list(map(lambda x : x * x, [1, 2, 3])))
print(list(map(lambda x, y, z : (x, y, z), [1, 2, 3], [1, 2], [1, 2, 3, 4])))
print(list(zip([0, 1, 2], [3, 4, 5])))
print(list(map(lambda x : x[0] + x[1], zip(range(5), range(5)))))
print(list(map(lambda x : x[0] + x[1], zip(range(5), range(5)))))
print(range(1, 10), range(1, 10)[2 : 8], range(1, 10).count(5), range(1, 10).index(7))
print(list(range(1, 10)))
print(isinstance(range(1, 10), range))
g = (i for i in range(0, 3))
print(next(g), next(g), next(g))
print(map(str, [1, 2, 3, 4, 5]), list(map(str, [1, 2, 3, 4, 5])))
i = 0
print([i for i in range(3)])
def fact(num):
    res = 1
    while num >= 1:
        res *= 1
        num -= 1
    return res
def fact(num):
    sleep(0.0001)
    math.factorial(num)
def xyz():
    return a, b
a, b = xyz()
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
"""				"""
a = 5
expr = "5 + 3 * a"
print(eval(expr))
a = b = c = 1
code = compile('a * b + c', '<string>', 'eval')
print(eval(code))
dic = {'a' : 7, 'b' : 6}
print(eval('a * b', dic))

import random as rn
print(rn.randint(1, 10))
print(rn.randrange(1, 10))
print(round(1.3), round(0.5), round(1.5), round(1.3), round(1.33, 1), round(0.5) , round(1.5), round(2.675, 2))
def sqrt(num):    
    print("I don't know what's the square root of {}.".format(num))
sqrt(4)
from math import *
x, y = 1.55, -1.55
print(pi, sin(1), sqrt(2), ceil(2.7))   
print(round(x), round(y), round(x + 1, round(y + 1)), floor(x), ceil(x), trunc(x))
import math
print(math.hypot(2, 4), math.radians(45), math.degrees(math.asin(1)), math.sin(math.pi / 2))
print(math.sin(math.radians(90)), math.asin(1), math.asin(1) / math.pi, math.cos(math.pi / 2))
import math
print(math.acos(1), math.tan(math.pi/2), math.atan(math.inf), math.atan(float('inf')))
print(math.atan2(1, 2), math.atan2(-1, -2), math.atan2(1, 0), math.sinh(math.pi), math.asinh(1))
print(math.cosh(math.pi), math.acosh(1), math.tanh(math.pi), math.atanh(0.5), math.log(math.e))
print(math.log(1), math.log(100), math.log(1 + 1e-20), math.log1p(1e-20), math.log10(10))
print(math.log(100, 10), math.log(27, 3), math.log(1, 10), math.copysign(-2, 3)   )
print(math.copysign(3, -3), math.copysign(4, 14.2), math.copysign(1, -0.0), math.floor(-1.7))
print(abs(1 + 1j), complex(1), complex(imag = 1), complex(1, 1), complex(1 + 1j), abs(1 + 1j))
import cmath
print(cmath.sqrt(-1), cmath.polar(1 + 1j), cmath.phase(1 + 1j), cmath.rect(math.sqrt(2), math.atan(1)))
print(cmath.phase(complex(-1.0, 0.0)), cmath.phase(complex(-1.0, -0.0)), cmath.log(1+1j), cmath.exp(1j * cmath.pi))
print(type(cmath.pi), cmath.isinf(complex(float('inf'), 0.0)), cmath.isnan(complex(0.0, float('nan'))), cmath.isinf(complex(0.0, math.inf)), cmath.isnan(complex(math.nan, 0.0)))
import cmath
z = cmath.rect(*cmath.polar(1 + 1j))  
x = 2 + 3j
print(cmath.isclose(z, 1 + 1j), cmath.phase(z), cmath.polar(z), cmath.rect(2, cmath.pi/2), cmath.exp(z), cmath.log(z))
print(cmath.log10(-100), cmath.sqrt(z), cmath.sin(z), cmath.cos(z), cmath.tan(z), cmath.asin(z), cmath.acos(z), cmath.atan(z))
print(cmath.sin(z)**2 + cmath.cos(z)**2,  cmath.sinh(z), cmath.cosh(z), cmath.tanh(z), cmath.asinh(z), cmath.acosh(z), cmath.atanh(z))
print(cmath.cosh(z)**2 - cmath.sin(z)**2,  cmath.cosh((0+1j)*z) - cmath.cos(z))
x = 2 + 3j
print(abs(x))
x.conjugate()
print(x)

from operator import *
print(add(1, 1), mul(2, 2), mul('a', 10)
,mul([3], 3))
#Bitwise operator
a, b = 10, -20
print(~a, ~b) #~n -> -|n+1|, ~-n -> |n-1|
c, d = 0, 1
print(c ^ d, c & d, bin(c | d), d << 5, bin(100 >> 2))
#inplace operation
a = 0b001; a &= 0b010; a |= 0b010; a <<= 2; a >>= 2; a ^= 0b011
print(a)
#Boolean
def or_(a, b):    
    if a: return a    
    else: return b
def and_(a, b):    
    if not a: return a    
    else: return b
print(or_(10, 15), and_(10, 15))
def T(): return True
def F(): return False
print(T() and F())
print(T() or F())
#compare
x = 3.141
if 3.14 < x < 3.142: print("x is near pi")
else: print("Outer")
#comparizon operator
if 1 > -1 < 2 > 0.5 < 100 != 24: print("Yes")
else: print("No")
print("alpha" < "beta")
print('12' != '1')
print('12' == 12)

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
print("Total students : %3d, Boys : %2d" % (240, 120))   
print("%7.3o" % (25)) 
print("%10.3E" % (356.08977))   # print exp
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
print(f"{'Geeks'} and {'Portal'}")
print('Number one portal is {0}, {1}, and {other}.' .format('Geeks', 'For', other ='Geeks'))
print("Geeks :{0:2d}, Portal :{1:8.2f}". format(12, 00.546))
print("Second argument: {1:3d}, first one: {0:7.2f}". format(47.42, 11))
print("Geeks: {a:5d},  Portal: {p:8.2f}". format(a = 453, p = 59.058))
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; ' 'Geeks: {0[geek]:d}'.format(tab))
data = dict(fun ="GeeksForGeeks", adj ="Portal")
print("I love {fun} computer {adj}".format(**data))
cstr = "I love geeksforgeeks"
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))
"""            """
name, age = "Alice", 30
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")
print("Name: %s, Age: %d" % (name, age))

value = 3.14159
print(f"{value:.2f}" ,"{:.2f}".format(value))
name = "Alice"
print("Hello, %s!" % name)
print('G','F','G', sep='')
print('09','12','2016', sep='-') 
print('G','F', sep='', end='') 
print('09','12','2016', sep='-', end='\n') 
print('prtk','agarwal', sep='', end='@') 
print('apples', 'oranges', 'bananas', sep=', ')
print('one', 'two', 'three', sep=';') 
print('????', '????', '????', sep='????') 

print(input("Enter your value: "))
print(input('What is your name?\n'))
num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
print ("type of number", type(num))
print ("type of name", type(name1))
num = int(input("Enter a number: "))
print(num, " ", type(num))
floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))
num = input("Enter a number: ")
num = int(num)
user_input = input("Enter something: ")
print(type(user_input))
user_input = input("Enter something: ")
print("You entered:", user_input)
import datetime
time_str = input("Enter a time (HH:MM:SS): ")
time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
print("Sum:", a + b + c)
x, y = map(float, input("Enter two floats separated by a space: ").split())
print("Product:", x * y)
name, age = input("Enter your name and age separated by a space: ").split()
print("Hello,", name + "! You are", age, "years old.")

x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
print([int(x) for x in input("Enter multiple values: ").split()])
print([int(x) for x in input("Enter multiple value: ").split(",")])

name, age = "John", 30
print("Name: ", name)
print("Age: ", age)
print("Hello, my name is", name, "and I am", age, "years old 
a, b = 10, 1000
print('The value of a is {} and b is {}'.format(a,b))
n = input('Enter the Number: ')
print(type(n))

import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end=' ', flush = True)
        time.sleep(1)
    else:
        print('Start')
print(10, 20, sep=' - ', 30)
a = [1, 2, 3, 4]
for i in range(4):
    print(a[i], end =" ") 
l = [1, 2, 3, 4, 5, 6]
print(*l)

import sys
sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!")

name, age = "Alice", 30
print("My name is", name, "and I am", age, "years old.", end=" ")
