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

