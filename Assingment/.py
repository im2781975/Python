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
