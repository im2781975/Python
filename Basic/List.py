num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = []
print(num[3], num[-3])
#start:end
print(num[2:6])
print(num[:])
print(num[1:])
print(num[:7])
#start:end:step
print(num[1:8:1])
print(num[1:8:2])
print(num[2:8:-1])
print(num[8:2:-1])
print(num[8:2:-2])
print(num[::-1])
num.append(5)
num.insert(6, -1)
print(num)
if 7 in num:
    num.remove(7)
print(num)
last = num.pop();
print(last, num)
if 6 in num:
    idx = num.index(6)
    print(idx)
sort = num.sort()
print(num)
num.reverse()
print(num)
for n in num:
    if n%2 ==1:
        odd.append(n)
print(odd)
odd_nums = [n for n in num if n%2 == 1 if n%5 == 0]
print(odd_nums)

player = ['A', 'B', 'C']
age = [21, 22, 23]
comb =[]
for p in player:
    print(p)
    for a in age:
        comb.append([p, a])
print(comb)
comb2 = [(p, a)for p in player for a in age ]
print(comb2)
