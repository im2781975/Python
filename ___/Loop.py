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
