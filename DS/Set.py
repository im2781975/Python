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


