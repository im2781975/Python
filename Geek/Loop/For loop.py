# Iterating over a String
print("String Iteration")

s = "Geeks"
for i in s:
    print(i)
////
for i in range(0, 10, 2):
    print(i)
////
l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)
////
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
////
# Python program to illustrate
# Iterating over a list
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)
////
Numbers =[x for x in range(11)]
print(Numbers)
////
# Iterating over dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
////
t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)
////
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)
////
# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
////
for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)
////
# An empty loop
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
////
# Python program to demonstrate
# for-else loop

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
////
clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print(f"Washing {paired_socks}")
////
for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
////
# Example 1: Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a string
for char in 'Python':
    print(char)

# Example 3: Using enumerate to get index and value
for index, num in enumerate([10, 20, 30]):
    print(f'Index {index}: {num}')

# Example 4: Iterating over a dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f'{key}: {value}')
////
# Example: Calculating sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f'Total sum: {total}')
////

