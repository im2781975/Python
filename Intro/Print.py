print("print\n('here i am')")
print("hi",input("what is your name:") + "," + "How are you?")

name = input("whats your name:")
length = len(name)
b = "molla"
print(name, length)
print(name + ' ' + b)
print("name[3]:", name[3])
print(5* "\njenny\'s \"Lectures\"")
#swap
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
tmp = a
a = b
b = tmp
print("Value of a is:", a)
print("Value of b is:", b)
#calculate bmi
weight = input("Entet weight: ")
height = input("Enter height: ")
bmi = int(weight)/float(height)**2
print(round(bmi, 2))
#left age
age = int(input("Enter age: "))
year_left = 90 - age
days_left = year_left*365
month_left = year_left*12
weeks_left = year_left * 52
print(f"you have left {days_left} days, {month_left} months, {weeks_left} weeks")
