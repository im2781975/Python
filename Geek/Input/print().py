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

