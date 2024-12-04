#password Generator
import string, random
letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letters =list(string.ascii_letters)
spaces = list(string.whitespace)
printable =list(string.printable)
digit =list(string.digits)
punctuation = list(string.punctuation)
print("Password Generator: \n")
l = int(input("Enter Number of letter: "))
d = int(input("Enter Number of digits: "))
p = int(input("Enter Number of punctuation: "))
password = []
for i in range(1, l + 1):
    char = random.choice(letter)
    password += char
for i in range(1, d + 1):
    char = random.choice(digit)
    password += char
for i in range(1, p + 1):
    char = random.choice(punctuation)
    password += char
random.shuffle(password)
print(password)
Generated = ""
for i in password:
    Generated += i
print(Generated)

#sum of the even num from 0 to 100
total = 0
#for i in range(0, 101, 2):
    #total += i 
for i in range(0, 101):
    if i % 2 == 0:
        total += i
print(total) 
#print numbers range(0, 100) where divisible by 3, 5, 3 and 5. instead of i print frizz, buzz, frizzbuzz
for i in range(101):
    if i % 3 == 0 and i % 5!= 0:
        print(i, "Fizz")
    elif i % 5 == 0 and i % 3 !=0:
        print(i, "Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    else:
        print(i)

#How many canes Of color need to paint a wall.(a cane max paint 7sq area )
import math
def PaintCalculation(height, weidth, coverage):
    area = height * weidth
    #NoOfCanes = round(area / coverage)
    NoOfCanes = math.ceil(area / coverage)
    print(f"{NoOfCanes} Canes need ")
h = int(input("Enter height: "))
w = int(input("Enter Weidth: "))
cover = 7
PaintCalculation(height = h, weidth = w, coverage = cover)

#prime checker
import math
def PrimeChecker(num):
    IsPrime = True
    if num == 1:
        IsPrime = False
    for i in range(2, math.ceil(num/2) + 1):
        if num % i == 0:
            IsPrime = False
    if IsPrime == True:
        print("Prime Number")
    else:
        print("Its not a prime number")
num = int(input("Enter number: "))
PrimeChecker(num)

#marks to grade
studentMarks = { "A":23, "B": 35, "C":78}
grade = {}
for i in studentMarks:
    marks = studentMarks[i]
    if marks > 90:
        grade[i] = "A+"
    elif marks > 80:
        grade[i] = "A"
    elif marks > 70:
        grade[i] = "B+"
    elif marks > 60:
        grade[i] = "B"
    elif marks > 50:
        grade[i] = "C"
    elif marks > 40:
        grade[i] = "D"
    else:
        grade[i] = "F"
print(grade)
    
    
