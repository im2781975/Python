A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6}
print(A.intersection(B))
#print(A & B)
print(A.union(B))
#print(A | B)
print(A.difference(B))
#print(A - B)
print(A.symmetric_difference(B))
#print(A ^ B)
print(A.issuperset(B))
#print(A >= B)
print(A.issubset(B))
#print(A <= B)
print(A.isdisjoint(B))
A.update(B)
#A |= B
print(A)
A.intersection_update(B)
#A &= B
print(A)
A.difference_update(B)
#A -= B
print(A)
print(len(A), len(B))
print(len(A & B) == 0)
print((A & B) == set())

#Existence check
print(2 in {1, 2, 3})
print(4 not in{1, 2, 3})

#Add or discard
A = {1, 2, 3, 4, 5}
A.add(6)
A.discard(7)
#if element not in set remove() give error
A.remove(2)
print(A)

#print unique element
A = [1, 2, 3, 1, 4, 5]
unique_A = set(A)
print(unique_A)
print(list(set(unique_A)))

