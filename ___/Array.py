import array as arr
b = arr.array('d', [2.9, 3.4, 5.2, 7.1])
for i in range(0, 4):
    print(b[i], end = " ")
print()
a = arr.array('i', [5, 9, 4, 1])
a.insert(1, 9); a.append(7)
print(a.pop(1))
for i in a:
    print(a.pop(), end = " ")
if 2 in a:
    a.remove(2)
for i in a:
    print(i, end = " ")
print("\r")
"""                """
lst = arr.array('i', [2, 3, 4, 5])
for i in range(0, 4):
    print(lst[i], end = " ")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = arr.array('i', lst)
for i in l:
    print(i, end = " ")
print(lst[3 : 8], lst[:], lst.index(5), lst.index(7))
arr = arr.array('i', [9, 8, 7, 6, 5, 4])
arr[2] = 2; arr[4] = 6
arr.extend([12, 13, 14, 15])
arr.reverse();
print(arr.count(6), *arr, arr.tolist())
for i in arr:
    print(i, end = " ")
print("\r")
"""                """
from array import array
arr = array('i', [1, 2, 3, 4, 5])
arr.remove(4) #del first occurance
ray = array('i', [7, 8, 9]); arr.extend(ray)
c = [11, 12, 13]; arr.fromlist(c)
print(arr.buffer_info, arr[0], arr.index(5))
for i in arr:
    print(i, end = ' ')
