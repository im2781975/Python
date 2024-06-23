#keyword
import keyword
 
# printing all keywords at once using "kwlist()"

print("The list of keywords is : ")

print(keyword.kwlist)

#Use
print(False == 0)

print(True == 1)
 

print(True + True + True)

print(True + False + False)
 

print(None == 0)

print(None == [])

#use
print(True or False)

print(False and True)

print(not True)

if 's' in 'geeksforgeeks':

    print("s is part of geeksforgeeks")

else:

    print("s is not part of geeksforgeeks")

for i in 'geeksforgeeks':

    print(i, end=" ")
 

print("\r")

print(' ' is ' ')

print({} is {})
 #loop
for i in range(10):
 

    print(i, end=" ")

    if i == 6:

        break
 

print()

i = 0

while i < 10:

    if i == 6:

        i += 1

        continue

    else:

        print(i, end=" ")
 

    i += 1
#if else
i = 20

if (i == 10):

    print("i is 10")

elif (i == 20):

    print("i is 20")

else:

    print("i is not present")
#def
def fun():

    print("Inside Function")
 
 
fun()
#class keyword
class Dog:

    attr1 = "mammal"

    attr2 = "dog"
 

    def fun(self):

        print("I'm a", self.attr1)

        print("I'm a", self.attr2)
 

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()
#factorial
import math as gfg
 

print(gfg.factorial(5))
#pass
n = 10

for i in range(n):
 

    # pass can be used as placeholder

    # when code is to added later

    pass
#lambda
# Lambda keyword

g = lambda x: x*x*x
 

print(g(7))
# Return keyword

def fun():

    S = 0
 

    for i in range(10):

        S += i

    return S
 
 

print(fun())
 
# Yield Keyword
 
 

def fun():

    S = 0
 

    for i in range(10):

        S += i

        yield S
 
 

for i in fun():

    print(i)
# import keyword

from math import factorial

import math

print(math.factorial(10))
 
# from keyword

print(factorial(10))
#try catch
a = 4

b = 0

try:

    k = a//b

    print(k)

except ZeroDivisionError:

    print("Can't divide by zero")
 

finally:

    print('This is always executed')
 

print("The value of a / b is : ")

assert b != 0, "Divide by 0 error"

print(a / b)
 

temp = "geeks for geeks"

if temp != "geeks":

    raise TypeError("Both the strings are different.")

#raise
temp = "geeks for geeks"

if temp != "geeks":

    raise TypeError("Both the strings are different.")
#del
my_variable1 = 20

my_variable2 = "GeeksForGeeks"

print(my_variable1)

print(my_variable2)

del my_variable1

del my_variable2

print(my_variable1)

print(my_variable2)
#global
a = 15

b = 10

def add():

    c = a + b

    print(c)
add()

def fun():

    var1 = 10
 

    def gun():

        nonlocal var1

         

        var1 = var1 + 10

        print(var1)
 

    gun()
fun()

 
