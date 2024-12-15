#keyword
import keyword
print(keyword.kwlist)
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
