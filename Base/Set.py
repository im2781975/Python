num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num)
number = set(num)
print(number)
number.add(10)
print(number)
if 5 in number:
    number.remove(5)
print(number)
for item in number:
    print(item)
A = {1, 2, 3}
B = {3, 4, 5, 6, 7}
print(A & B)
print(A | B)
