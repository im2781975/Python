car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
def findSmaller(tup):
    print('Check {0}, {1}$'.format(*tup)) 
    return tup[1] < 100  
result = next(filter(findSmaller, car_shop), None)
print("Result:", result)
generator = (car for car in car_shop if not car[1] < 100) 
next(generator)
"""                """

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

def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
divide(3, 2)
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
divide(3, 0)
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        print("The error is: ",e)
divide(3, "GFG") 
divide(3,0) 
def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
try: 
    k = 5//0 
    print(k) 
except ZeroDivisionError:    
    print("Can't divide by zero") 
finally:
    print('This is always executed')
print(help("modules"))
print(help("random"))

print(len("jenny"))
lst = ["jenny", 7]; print(len(lst))
dic = {1 : "A", 2 : "B", 3 : " C"}; print(len(dic))
line = ord('\n'); print(f"newline: {line} ", f"{{Double Braces}} ")
print('''Molla'4'Now''')
