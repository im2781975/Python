def unpacking(a


a, b = 10, 20
print("Both are Equal" if a == b else "a is greater" if a > b else "b is greater")
print(("b is minimum", "a is minimum")[a < b])
print({True : "a is minimum", False: "b is minimum"}[a < b])
print((lambda: "b is minimum", lambda: "a is minimum")[a < b]())
print(a, "is minimum") if(a < b) else print(b, "is minimum")
maxi = a if a > b else b
Dict = {'max' : a if a > b else b}
res = "Positive" if a > 0 else "negetive"

#isinstance
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
print(i)
#control statement
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
    if cnt == 7:
        #continue
        break
    print("inner loop")
print("outer loop")

cnt = 0
while cnt < 3:
    cnt += 1
    print("Hi")
    
#range
for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)

for i in range(5):
    print("a")
    print("b")
    if i == 2:
        print("Welcome")
        if True:
            print("Hello")
print("Bye")

def display():
    for i in range(1, 11):
        print(i)
display()

#in, not, not in, is, is not
#or, and
boss = True
if boss is True or boss is not False:
    print("True")
else:
    print("False")
coin = 'head'
if boss = False:
    print("False")
    if coin == 'tail':
        print("Batting")
    else:
        print("Bowling")
        
a = 23
if a > 5:
    if a % 2 == 0 and a > 7:
        print("Even")
    else:
        print("Odd")
else:
    print("less than 5")
    
num = 1
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
    if num == 8:
        break

i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end = " ")
    i += 1

#for i  in range(1, 11):
#range[start, end, step]
for i in range(1, 11, 2):
    print(i)

name, cog = ['Aa', 'Bb', 'Cc'], 'Molla'
for i in name:
    print(i)
    if i == 'Bb':  print("Hey")
for x in cog:
    print(x)
    
tes, lst = {2, 3, 5, -2, 10}, [2, 3, 5, -2, 10]
sq, sqr = set(), []
for i in tes:
    square = i ** 2
    sq.add(square)
    print(sq)
for i in lst:
    sq = i**2
    sqr.append(sq)
    print(sqr)
print(f"set: {sq}\nlist: {lst} ")

cnt = 1
while cnt <= 10: print(cnt); cnt += 1
cnt = 5
while cnt >= 5: print(cnt); cnt -= 1
lst = [2, 3, 4, 5]
while lst: print(lst, "Hi"); lst.pop()
"""             """
cnt = 1
#while cnt <= 5:
while True:
    print(cnt)
    cnt += 1
    if cnt == 2:
        break
else:
    print("Outer block")
print("End")
"""             """
cnt = 1
while cnt <= 5:
    print(cnt)
    cnt += 1
else:
    print("Outer block")
print("End")

#sentinal value
num = int(input("Enter val(-1 for exit): "))
while num != -1:
    print(num)
    num = int(input("Enter val(-1 for exit): "))
else:
    print("Outer Block")
print("End")
"""             """
total = 0
num = int(input("Enter val(-1 for exit): "))
while num != -1:
    total += num
    num = int(input("Enter val(-1 for exit): "))
print(total)
"""                """
rang = range(5)
print(f"rang: {rang}\nrang[1]: {rang[1]} ")
rang = range(2, 10, 2)#(start, end, stp)
for i in rang:
    print(i, rang)
for i in range(10, 0, -2):
    print(i, rang)
    
def table(n):
    for i in range(1, 11):
        print(i * n, end = " ")
table(5)
#sum of even
total = 0
#exclude 100 sum even
for i in range(0, 100, 2):
    total += i
print(total)

i = 25
if i == 10: print("i is 10")
elif i == 15: print("i is 15")
elif i == 20: print("i is 20")
else: 
    print("i isn't present")
"""                 """
i = 10
print(True) if i < 15 else print("False")
"""                 """
x = 0
res = { x > 0 : "positive", x < 0 : "negatives "}.get(True, "zero")
print(res)
x = 0
{x > 0 : print("positive"), x < 0 : print("negetive")}.get(True, print("Zero"))
"""                 """
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B, C")
"""             """
num = 10
if num > 5:
    print("greater than 5")
    if num <= 15:
        print("Between 5 & 15")
"""                 """
i = 0
if i != 0:
    if i > 0:
        print("positive")
    else:
        print("Negetive")
else:
    print("Zero")
"""                    """
def match():
    num = int(input("Enter choice: "))
    match num:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case _:
            print("Not Between 1 & 3")
def match():
    num = int(input("Enter choice: "))
    match num:
        case 1 | 2:
            print("One Or Two")
        case 3 | 4:
            print("Three Or Four")
        case 5 | 6:
            print("Five Or Six")
        case _:
            print("Not Between 1 & 6")
def match():
    num = int(input("Enter choice: "))
    match num:
        case num if num > 0:
            print("Positive")
        case num if num < 0:
            print("Negetive")
        case _:
            print("Zero")
def match():
    ing = "Hellow vai"
    match(ing[6]):
        case "w":
            print("case 1 match")
        case "W":
            print("case 2 match")
        case _:
            print("char not in the string")
def match(val):
    match val:
        case 1:
            return "val is 1"
        case 2:
            return "val is 2"
        case 3:
            return "val is 3"
        case _:
            return "else"
print(match(1))
print(match(2))
def match(ing):
    match ing:
        case ["a"] :
            print("a")
        case ["a", *b]:
            print(f"a and {b} ")
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e ")
        cese _:
            print("No data")
match([])
match(["a"])
match(["a", "b"])
match(["b", "c", "d", "e"])
"""             """
def runMatch(dictionary):
    match dictionary:
        case {"name": n, "age": a} if "salary" not in dictionary:
            print(f"Name: {n}, Age: {a}")
        case {"name": n, "salary": s} if "age" not in dictionary:
            print(f"Name: {n}, Salary: {s}")
        case {"name": n, "age": a, "salary": s}:
            print(f"Name: {n}, Age: {a}, Salary: {s}")
        case {"age": a} | {"salary": s}:
            print("Error: Name is missing in the data.")
        case _:
            print("Data does not match any known patterns.")
runMatch({"name": "Jay", "age": 24})            
runMatch({"name": "Ed", "salary": 25000})  
runMatch({"name": "Al", "age": 27, "salary": 30000})
runMatch({"age": 30})
runMatch({})            
"""             """
from dataclasses import dataclass
@dataclass
class person:
    name : str
    age : int
    salary: int
@dataclass
class programmer:
    name : str
    lang : str
    framework : str
def runMatch(instance):
    match instance:
        case Programmer("Om", language="Python", framework="Django"):
            print(f"Name: Om, Language:Python, Framework:Django")
        case Programmer("Rishabh", "C++"):
            print("Name:Rishabh, Language:C++")
        case Person("Vishal", age=5, salary=100):
            print("Name:Vishal")
        case Programmer(name, language, framework):
            print(f"Name:{name}, Language:{language}, Framework:{framework}")
        case Person():
            print("He is just a person !")
        case _:
            print("This person is nothiing!")
programmer1 = Programmer("Om", "Python", "Django")
programmer2 = Programmer("Rishabh", "C++", None)
programmer3 = Programmer("Sankalp", "Javascript", "React")
person1 = Person("Vishal", 5, 100)
runMatch(programmer1)
runMatch(programmer2)
runMatch(person1)
runMatch(programmer3)

"""            """
a, b, c = 0, 2, 4
if a > b or b < c:
    print("True")
else:
    print("False")
if a or b or c:
    print("\nAtleast one value has boolean true")
if a and b and c:
    print("\nAll number has boolean true")
else:
    print("\nAtleast one has boolean true")

"""                """
a = 0
if not a:
    print("\na is true")
#equivalent
b = 1
if(a == 0):
    print("a == 0: ", a == 0)
if(a == b):
    print("a == b", a == b)
if(a!= b):
    print("a != b", a != b)
"""            """
x, y = 10, 10
if(x is y):
    print("True")
else:
    print("False")
"""				"""
for i in range(5, 20, 2):
    print(i, end = " ")
print()
for i in range(25, 2, -2):
    print(i, end = " ")
print()
val = range(10)[0] #first
val = range(10)[-1] #last element
print(val)
from itertools import chain
res = chain(range(5), range(10, 20, 2))
print(res)
for i in res:
    print(i, end = " ")
print()
fruits = ["A", "B", "C", "D"]
for i in range(len(fruits)):
    print(fruits[i], i, end = " ")
"""					"""
ing = "mollavai"
for letter in ing:
    print(letter, end = ' ')
    if letter == 'a' or letter == 'i':
        break
print()
i = 0
while(True):
    print(ing[i], end = ' ')
    if ing[i] == 'a' or ing[i] == 'i':
        break
    i += 1
"""                """
print()
for i in range(1, 5):
    for j in range(2, 6):
        if j % i == 0:
            break
        print(i, ' ', j)
"""                 """
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end = ' ')
"""                   """
print()
for i in ing:
    if i == 'o':
        print("Executed")
        pass
    print(i, end = " ")
"""					"""
n = 5
print("Hello") if n > 10 else print("Bye") if n > 5 else print("GoodBye")
a = 1 
if a == 3 or 4 or 6:
    print('yes')
else:
    print('no')
if a in (3, 4, 6): 
    print('yes') 
else:
    print('no')
"""					"""
i = 0
while i < 7:
    print(i, end = " ")
    if i == 4:
        break
    i += 1
"""                """
print()
for i in (0, 1, 2, 3, 4, 5):
    print(i, end = " ")
    if i == 2:
        break
"""                 """
print()
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i, end = " ")
"""                 """
print()
def breakLoop():
    for i in range(1, 5):
        if i == 2:
            return i
        print(i)
    return (5)
"""                 """
print()
def breakAll():
    for j in range(1, 5):
        for i in range(1, 4):
            if i * j == 6:
                return (i)
            print(i * j)
"""                    """
print()
for i in [0, 1, 2, 3, 4]:
    print(i, end = ' ')
print()
for i in range(5):    
    print(i, end = ' ')
print()
for i in ['One', 'Two', 'Three', 'Four']:
    print(i, end = ' ')
print()
for i in range(1, 6):
    print(i, end = ' ')
print()
for index, item in enumerate(['one', 'two', 'three', 'four']):   
    print(index, '::', item, end = ' ')
print()
x = map(lambda e : e.upper(),['one', 'two', 'three', 'four']) 
print(x, end = ' ')
"""                    """
print()
for i in range(3):
    print(i,  end = " ")
else:
    print("done")
print()
i = 3
while i < 3:
    print(i, end = ' ')
    i += 1
else:
    print("done")
"""                    """
lst = [1, 2, 3, 4]
for i in lst:
    if type(i) is not int:
        print(i, end = ' ')
        break
    else:
        print("No exeception")
"""                """
print()
"""                """
a = 10
while True:
    a -= 1
    print(a, end = " ")
    if a < 7:
        break
print("Done")
"""						"""
ing = "Geeks"
for i in ing:
    print(i, end = " ")
l1 = ["eat", "sleep", "repeat"]
for count, ele in enumerate(l1):
    print (count, ele)
"""            """
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
lst = ["geeks", "for", "geeks"]
for i in lst:
    print(i, end = " ")
print([x for x in range(11)])

d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
tup = ((1, 2), (3, 4), (5, 6))
for a, b in tup:
    print(a, b)

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
for i in range(1, 4):
    print(i)
else:  
    print("No Break\n")
    
clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print(f"Washing {paired_socks}")
for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
    
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
for char in 'Python':
    print(char)
for index, num in enumerate([10, 20, 30]):
    print(f'Index {index}: {num}')
    
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f'{key}: {value}')

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f'Total sum: {total}')

count = 0
while (count < 3): 
    count = count + 1
    print("Hello Geek")
    
age = 28
while age > 19: 
    print('Infinite Loop')
    break

i = 0
a = 'geeksforgeeks'
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

i = 0
a = 'geeksforgeeks'
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        break
    print('Current Letter :', a[i]) 
    i += 1

a = 'geeksforgeeks'
i = 0
while i < len(a): 
    i += 1
    pass
print('Value of i :', i) 

i = 0
while i < 4: 
    i += 1
    print(i) 
else:  
    print("No Break\n") 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
    break
else: 
    print("No Break") 
    
a = int(input('Enter a number (-1 to quit): ')) 
while a != -1: 
    a = int(input('Enter a number (-1 to quit): '))
    
count = 0
while True: 
    count += 1
    print(f"Count is {count}") 
    if count == 10:
        break
a = [1, 2, 3, 4] 
while a: 
    print(a.pop())

count = 0
while (count < 5): 
    count += 1
    print("Hello Geek") 

initial_height = 10 
bounce_factor = 0.5 
height = initial_height 
while height > 0.1:   
    print("The ball is at a height of", height, "meters.") 
    height *= bounce_factor   
print("The ball has stopped bouncing.")

countdown = 10
while countdown > 0: 
    print(countdown) 
    countdown -= 1
print("Blast off!") 
