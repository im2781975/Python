name = "John"
age = 30

print("Name:", name)
print("Age:", age)

#print works
name = "Alice"
age = 25

print("Hello, my name is", name, "and I am", age, "years old.")

#----
a,b,=10,1000
print('The value of a is {} and b is {}'.format(a,b))
#---
n = input('Enter the Number: ')

print('Number Entered by User:',n)

print(type(n))
#-----
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')
#----
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('Start')
#-----
a=12
b=12
c=2022
print(a,b,c,sep="-")
#-----
print(10, 20, sep=' - ', 30)
#----
# Python 2 code for printing
# on the same line printing
# geeks and geeksforgeeks 
# in the same line
 
# Without newline
print("geeks"),
print("geeksforgeeks")
 
# Array
a = [1, 2, 3, 4]
 
# Printing each element on the same line
for i in xrange(4):
    print(a[i]),
#--++--
# Python 3 code for printing
# on the same line printing 
# geeks and geeksforgeeks 
# in the same line
 
print("geeks", end =" ")
print("geeksforgeeks")
 
# array
a = [1, 2, 3, 4]
 
# printing a element in same
# line
for i in range(4):
    print(a[i], end =" ") 
#----
# Print without newline in Python 3.x without using for loop
 
l = [1, 2, 3, 4, 5, 6]
 
# using * symbol prints the list
# elements in a single line
print(*l)
#-----
import sys
 
sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!")
#++++

