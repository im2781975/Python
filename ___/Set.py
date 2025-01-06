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
