cnt = 1
while cnt <= 10:
    print(cnt)
    cnt+= 1
    if cnt == 7:
        break
    print("Remain")
print("Outer loop")

list1 = [1, 2, 3, 4, 6]
list2 = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
for item in list1:
    for name in list2:
        print(item, name)
        if item == 4 and name == 'Dd':
            break
    print("Out From inner loop")
print("Out from the loop")
#continue
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt+= 1
    if cnt == 7:
        continue
    print("Remain")
print("Outer loop")

for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)
#pass
for i in range(1, 11):
    pass
