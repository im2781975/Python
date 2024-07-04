# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}
tup1 = (1, 2, 3, 4, 5)

# using membership 'in' operator
# checking an integer in a list
print(2 in list1)

# checking a character in a string
print('O' in str1)

# checking an integer in aset
print(6 in set1)

# checking for a key in a dictionary
print(3 in dict1)

# checking for an integer in a tuple
print(9 in tup1)
////
#  Define a function() that takes two lists
def overlapping(list1, list2):

    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if(list1[i] == list2[j]):
                return 1
    return 0


list1 = [1, 2, 3, 4, 5]
list2 = [6, 2, 8, 9]
if(overlapping(list1, list2)):
    print("overlapping")
else:
    print("not overlapping")
////
# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}
tup1 = (1, 2, 3, 4, 5)

# using membership 'not in' operator
# checking an integer in a list
print(2 not in list1)

# checking a character in a string
print('O' not in str1)

# checking an integer in aset
print(6 not in set1)

# checking for a key in a dictionary
print(3 not in dict1)

# checking for an integer in a tuple
print(9 not in tup1)
////
# import module
import operator

# using operator.contain()
# checking an integer in a list
print(operator.contains([1, 2, 3, 4, 5], 2))

# checking a character in a string
print(operator.contains("Hello World", 'O'))

# checking an integer in aset
print(operator.contains({1, 2, 3, 4, 5}, 6))

# checking for a key in a dictionary
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))

# checking for an integer in a tuple
print(operator.contains((1, 2, 3, 4, 5), 9))
////
# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

str1 = "hello world"
str2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is num2)
print(lst1 is lst2)
print(str1 is str2)
print(str1 is str2)
////
# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

str1 = "hello world"
str2 = "hello world"

# using 'is not' identity operator on different datatypes
print(num1 is not num2)
print(lst1 is not lst2)
print(str1 is not str2)
print(str1 is not str2)
////
