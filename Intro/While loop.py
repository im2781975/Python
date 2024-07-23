count = 1
while count <= 5: print(count);count += 1
cnt = 5
while cnt >= 0: print(cnt); cnt -= 1
list1 = [2, 3, 4, 5, 6]
while list1:
    print(list1,"Hi")
    list1.pop()
    
#while-else
cnt = 1
while(cnt <= 5):
    print(cnt)
    cnt += 1
    if cnt == 3:
        break
else:
    print("Else block")
print("Outer loop")

cnt = 1
while(cnt <= 5):
    print(cnt)
    cnt += 1
else:
    print("Else block")
print("Outer loop")
#sentinal val
num = int(input("Enter num(-1 for exit): "))
while num != -1:
    print(num)
    num = int(input("Enter num(-1 for exit: "))
else:
    print("Else block")
print("Outer loop")

cnt = 1
while True:
    print(cnt)
    cnt += 1
    if cnt == 5:
        break
else:
    print("Else Block")
print("Out Of Bound")

total = 0
num = int(input("Enter integer(0 For Exit): "))
while num !=0:
    total += num
    num = int(input("Enter integer(0 For Exit): "))
print(total)
