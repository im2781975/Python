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
