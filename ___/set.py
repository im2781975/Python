
set1 = {10, 56, 89, 90, True, 'Molla', 1}
#1 & True return same value
set1.add(99)
set1.remove(90)
set1.discard(68) #if not present it will return no error
for i in range(1, 6):
    set1.add(i)
for i in range(1, 5):
    set1.remove(i)
print(set1, len(set1))
print(set1.pop())
set1.add((13, 14, 15))
#set1.add([16, 17, 18])
#not work for immutable
print(set1)
set1.clear()
set2 = {} 
set2.clear()
set3 = set()
print(type(set1), type(set2), type(set3))
set1 = {1, 2, 3, 4 }
set2 = {3, 4, 5, 6 }
set3 = set()
print(f"Union is: {set1.union(set2)} ")
#print(f"Union is: {set2.union(set1)} ")
#print(f"Union is: {set1 | set2} ")
print(set1.union((10, 11)))
set1.update(set2)
#set1|= set2
set1.update([29, 30])
print(set1)

print(set1.intersection(set2, set3))
#print(set1.intersection([19, 20]))
#print(set1.intersection(set2))
#print(set1 & set2)
#print(set1 & set2 & set3)

set1.intersection_update(set2)
print(set1)
print(set1.difference(set2, set3))
#print(set1.difference((10, 11)))
#print(set1 - set2)
set1.difference_update(set2)
print(set1)
set1.symmetric_difference(set2)
#method take maximum one agr
#(set1 | set2) - (set1 & set2)
#print(set1 ^ set2 ^ set3)
set2.symmetric_difference_update(set1)
set2.symmetric_difference_update((11, 15))
print(set2)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 10, 7, 8, -10}
print(set1.isdisjoint(set2))
print(set1.isdisjoint((['Hakim', 'sakib'])))
#method
print(set1.issubset(set2))
#print(set1 <= set2)
print(set1.issuperset(set2))
#print(set1 >= set2)
set2.clear()
#del set2
#it will remove whole set
print(set2)
st = set(); print(st)
st = set("Molla vai"); print(st)
ing = "Here i am"
st = set(ing); print(st)
st = set(["Mah", "Abd"]); print(st)
print("Abd" in st)
tup = ("Mah", "Abd"); print(set(tup))
dic = {"Abdullah" : 1, "Al" : 2, "Arifin" : 3}; print(set(dic))
tes = set([1, 2, 4, 4, 3, 3, 3, 6, 5]); print(tes)
tes = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']); print(tes)
tes = {1, 2, 3}; print(tes)
st = set([4, 5, (6, 7)]); st.update([10, 11])
print(st)
#Frozen set
ing = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
fset = frozenset(ing); print(fset)
print(frozenset())
lst = [1, 2, 3, 3, 4, 5, 5, 6, 2]; print(set(lst))
#set is muteable(mean can add or remove) but frozen is immuteable
#set print unique elements
st = {'A', 'B', 'C', 'D', 'B'}
tes = set('abcde')
tes.add('z')
print(tes, st)
frset = frozenset("Mollvai")
print(frset)
"""						"""
strset = set("mollavai")
lstset = set([1, 2, "am", "ironman", 6, 9])
print(f"strset: {strset}\nlstset: {lstset}\n")
for i in lstset:
    print(i, end = " ")
"""						"""
st = {1, 2, 3}
i = iter(st)
print(i, next(i), next(i))
for a in st:
    print(a, end = " ")
lst = list(st)
tsl = [a * 2 for a in st if a > 2]  
print(tsl)
"""				"""
A, B = {1, 2, 3, 4, 5}, {3, 4, 5, 6}
print(A.intersection(B), A.union(B)) #(A & B,A | B)
print(A.difference(B), A.symmetric_difference(B))#(A - B, A ^ B)
print(A.issuperset(B), A.issubset(B)) #(A >= B, A <= B)
print(A.isdisjoint(B))
A.update(B), print(A) # A |= B
A.intersection_update(B), print(A) # A &= B
A.difference_update(B), print(A) # A -= B
print(len(A), len(B))
print(len(A & B) == 0, (A & B) == set())
#Existance
print(2 in {1, 2, 3}, 4 not in {1, 2, 3})
"""            """
A = {1, 2, 3, 4, 5, 6}
A.add(7), A.discard(5), print(A)
if 3 in A:
    A.remove(3)
"""            """
A = [1, 2, 3, 1, 4, 5]
print(set(A), list(set(A)))
from collections import Counter
cnt = Counter(['A', 'B', 'C', 'B'])
print(cnt)
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = set(number)
num.add(10)
if 5 in num: num.remove(5)
print(num)
for i, item in enumerate(num):
    print(i, item)

A, B = {1, 2, 3}, {3, 4, 5, 6, 7, 8}
print(f"A & B: {A & B}\nA | B: {A | B} ")
comb = {}
comb = {(x, y)for x in A for y in B}
print(comb)
