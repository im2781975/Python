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
