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
# split a balanced string which consists ['R', 'L'] into maximum number of 
# strings such that the new strings are also balanced.
def split(ing):
    cnt = cntX = cntY = 0
    balanced = []
    for ch in ing:
        if ch == 'L':
            cntX += 1
        elif ch == 'R':
            cntY += 1
        if cntX == cntY:
            balanced.append(ing[:cntX + cntY])
            cnt += 1
            ing = ing[cntX + cntY:]
            cntX = cntY = 0
    return cnt, balanced
ing = input().strip()
cnt, balanced = split(ing)
print(cnt)
for rin in balanced:
    print(rin, end = " ")
# from a sequence of positive integers have to remove some of the elements so that it will be a good sequence.
# sequence b is a good sequence when each element of x in b, occurs exactly x times in b.
# Find the minimum number of elements that needs to be removed so that it will be a good sequence.
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
mp = defaultdict(int)
for num in a:
    mp[num] += 1
ans = 0
for num, count in mp.items():
    if count < num:
        ans += count
    else:
        ans += count - num
print(ans)
#Minimize a number
def maxi(N, x):
    cnt = 0
    while all(num % 2 == 0 for num in x):
        x = [num // 2 for num in x]
        cnt += 1
    return cnt
num = int(input(""))
ing = input("")
lst = list(map(int, ing.split()))
print(maxi(num, lst))
#Freq array
n, m = map(int, input().split())
num = list(map(int, input().split()))
freq= [0] * (m + 1)

for i in num:
    freq[i] += 1
for val in freq[1:]:
    print(val)

