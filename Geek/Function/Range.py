for i in range(5):
    print(i, end=" ")
print()
////
# printing first 6
# whole number
for i in range(6):
    print(i, end=" ")
print()
////
# printing a natural
# number from 5 to 20
for i in range(5, 20):
    print(i, end=" ")
////
for i in range(0, 10, 2):
    print(i, end=" ")
print()
////
# incremented by 4
for i in range(0, 30, 4):
    print(i, end=" ")
print()
///
# incremented by -2
for i in range(25, 2, -2):
    print(i, end=" ")
print()
////
# using a float number
for i in range(3.3):
    print(i)
////
from itertools import chain
 
# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))
 
for i in res:
    print(i, end=" ")
////
ele = range(10)[0]
print("First element:", ele)
 
ele = range(10)[-1]
print("\nLast element:", ele)
 
ele = range(10)[4]
print("\nFifth element:", ele)
////
fruits = ["apple", "banana", "cherry", "date"]
 
for i in range(len(fruits)):
    print(fruits[i])
