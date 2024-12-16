#list is Muteable
#Assign & access value 
x = y = [12, 13, 14]
x = [9, 10, 11]
y[0] = -1
print(f"x:{x}, y:{y}")
x = [1, 2, 3, [4, 5, 6], 7]
print(f"x:{x},\nx[3]:{x[3]}, \nx[3][2]:{x[3][2]} ")

lst = [1, 3.60, 'Hello', 'd']
tisl = ["Hello", "world"]
lst += tisl
print(lst, lst[0 : 2], lst * 2)
#insert
name = ['A', 'B', 'C', 'D', 'E']
name.insert(1, 'F')
print(len(name))
name.reverse()
if 'B' in name:
    name.remove('B')
for i in name:
    print(i)
print(name.count('A'))
print(f"name: {name}, \nname.index[F]: {name.index('F')} ")

l1 = [1, 2, 3, 4, 5]
l2 = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
for item in l1:
    for name in l2:
        print(item, name)
        if item == 4 and name == 'Cc':
            break
    print("Inner")
print("outer")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = []
for n in num:
    if n % 2 == 1:
        odd.append(n)
#odd = [n for n in num if n % 2 == 1 if n % 5 == 0]
print(odd)

player, age = ['A', 'B', 'C'], [21, 22, 23]
comb = []
for p in player:
    for a in age:
        comb.append([p, a])
#comb = [(p, a)for p in player for a in age]
print(comb)

number = [5, 10, 15, 20]
sum = 0
for num in number:
    sum += num
    print(num)
    if sum > 20:
        print(f"{sum} is Greater than 20")
print(sum)
for i in number[:]:
    sum += i
    number.append(sum)
print(number)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
E = map(lambda x : x * x, num)
print(list(E))
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[3], num[-3])
#start : end
print(f"num[:] {num[:]}\nnum[2:] {num[2:6]}\nnum[1:] {num[1:]}\nnum[:7] {num[:7]} ")
#start : end : range
print(f"num[1:8:1] {num[1:8:1]}\nnum[1:8:2] {num[1:8:2]}\nnum[2:8:-1] {num[2:8:-1]}\nnum[8:2:-1] {num[8:2:-1]}\nnum[8:2:-1] {num[8:2:-2]}\nnum[::-1] {num[::-1]} ")
num.append(100)
num.insert(6, -1)
if 5 in num: num.remove(5)
print(num)
if 6 in num:
    idx = num.index(6) 
    print(idx)
print(num.pop(), num)
num.sort() 
num.reverse()
print(num)
print(f"length is: {len(num)} ")
print(f"list is: {num}\nMaximum is: {max(num)}\nMinimum is: {min(num)} ")
num.append(45)
num.extend([46, 47, 48]) #For append more value
num[1] = -1 
num[2 : 4] = [49, 50, 51]
x = int(input("Enter integer: "))
if x in num: 
    num.remove(x)
else: 
    print("Doesn't exit")
print(num.sort()) #output : None
#num.remove(x) remove first occurance
print(num.pop())
print(num.pop(1))#num.pop(idx)
print(num.count(0))
print(num)
#nested
num = [1, 10, 15, [20, -10, 15], 17, -20]
print(len(num))
print(f"num[3][1]: {num[3][1]}\nnum[len(num) - 1]: {num[len(num) - 1]}\nnum[3][0 : 3]: {num[3][0 : 3]}\nnum[3][-1 : 3]: {num[3][-1: 3]}\nnum[3][::-1]: {num[3][::-1]}\n ")
num = [1, 10, 15, ["Aa", "Bb", "Cc"], 17, -20]
print(f"num[3][1]: {num[3][1]}\nnum[len(num) - 1]: {num[len(num) - 1]}\nnum[3][0 : 3]: {num[3][0 : 3]}\nnum[3][-1 : 3]: {num[3][-1: 3]}\nnum[3][::-1]: {num[3][::-1]}\n ")
