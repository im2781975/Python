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
