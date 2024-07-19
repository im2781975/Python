tuple1 = (1, 7, -4, "jenny", True,7, -5)
tuple2 = (10, 12, 14, 16)
tuple3 = (11,)
#For print type have to add (,)last.
#tuple are immutable
print(tuple1, tuple1[1], tuple1[-2], tuple1[-5], tuple1[0])
print(tuple1[1:3])
print(tuple1[:5], len(tuple1))

print(type(tuple2), type(tuple3))
tuple4 = (tuple1, tuple2, tuple3)
print(tuple4)
print(len(tuple4), tuple4[0])
#For concatenate all the tuple should be same type
tuple4 = tuple1 + tuple2 + tuple3
print(len(tuple4))
print(tuple4)
#Should be same elements not mixed
print(max(tuple2), min(tuple2))
print(tuple2.count(12))
print(tuple2.index(12))
#convert list to tuple
list1 = [2, 3, 4, 5]
print(tuple(list1))
tuple6 = (10,)*6
tuple7 = ("Molla",)*6
print(tuple6, tuple7)
