set1 = {10, 56, 89, 90, True, 'Molla', 1}
#1 & True return same value
set1.add(99)
set1.remove(90)
set1.discard(68) #if not present it will return no error
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
