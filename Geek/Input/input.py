# Python program showing 
# a use of input()

val = input("Enter your value: ")
print(val)
#----
name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
print(name) 
#----
# Program to check input 
# type in Python

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))
#----
# Python program showing
# a use of raw_input()

g = raw_input("Enter your name : ")
print g
#-----
num = int(input("Enter a number: "))
print(num, " ", type(num))

          
floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))

                 
#----
# Input a number
num = input("Enter a number: ")
# Convert input to integer
num = int(num)
#-----
user_input = input("Enter something: ")
print(type(user_input))
#-----
user_input = input("Enter something: ")
print("You entered:", user_input)
#-----
import datetime
# Input time as string
time_str = input("Enter a time (HH:MM:SS): ")
# Convert string to datetime object
time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
#----
# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
#----
#Example with integers
a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
print("Sum:", a + b + c)

#Example with floats:
x, y = map(float, input("Enter two floats separated by a space: ").split())
print("Product:", x * y)

#Example with strings:
name, age = input("Enter your name and age separated by a space: ").split()
print("Hello,", name + "! You are", age, "years old.")
#-----
# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))

# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 
#-----
# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x) 
#----

