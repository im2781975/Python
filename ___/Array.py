import array as arr
b = arr.array('d', [2.9, 2.3, 8.9])
print("Elements of float are: ")
for i in range(0, 3):
    print(b[i], end = " ")
    
"""                """
print()
a = arr.array('i', [1, 2, 3])
a.insert(1, 9) #insert(idx, val)
a.append(19) #append(val)
print("Elements of integer are: ")
for i in a:
    print(i, end = " ")
print()
print(f"a[0]: {a[0]}\na[1]: {a[1]} ")
print(f"a.pop(): {a.pop()}\na.pop(2): {a.pop(2)} ")
if 2 in a:
    a.remove(2)
for i in a:
    print(i, end = " ")
print("\r") #double tap

"""            """
lst = arr.array('i', [2, 3, 1, 5, 4])
for i in range(0, 5):
    print(lst[i], end = " ")
print()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = arr.array('i', lst)
for i in l:
    print(i, end = " ")
print(f"\nlst[3 : 8]: {lst[3 : 8]}\nlst[5 : ]: {lst[5 : ]}\nlst[:]: {lst[:]} ")
print(f"first occurance of \nlst.index[5]: {lst.index(5)}\nlst.index[7]: {lst.index(7)} ")
for i in l:
    print(i, end = " ")
arr = arr.array('i', [9, 8, 7, 6, 5, 4])
arr[2] = 6
arr[4] = 8
print("\narray is: ")
for i in range(0, 5):
    print(arr[i], end = " ")
print(f"\narr.count(6): {arr.count(6)}")
arr.reverse()
print("Reverse array is: ",*arr)
arr.extend([12, 13, 14, 15])
for i in arr:
    print(i, end = " ")
    
"""                """
import array as arr
print()
b = arr.array('d', [2.4, 4.5, 8.9])
for i in range(0, 3):
    print(b[i], end = " ")
b.extend([2.9, 3.7, 5.9])
print()
for i in b:
    print(i, end = " ")
