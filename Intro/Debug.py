def display():
    for i in range(1, 11):
        if i == 10:
            print(i)
display()

import random
DiceNum = ["One", "Two", "Three", "Four", "Five", "Six"]
num = random.randint(0, 5)
print(DiceNum[num])

year = int(input("Birth Year: "))
if year > 1980 and year <= 1996:
    print("Millenial")
elif year > 1996:
    print("Gen Z")
    
age = int(input("Enter age: "))
if age >= 18:
    print("Can vote")
else:
    print("cant vote")
    
a,b = 0,0
a = int(input("Enter a: "))
b = int(input("Enter b: "))
mult = a * b
print(mult)
