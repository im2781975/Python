# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: ")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with the use of a tuple
t = ("Geeks", "for", "Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print("\nSet with the use of Dictionary: ")
print(set(d))
///
# Creating a Set with a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

# Creating a Set with a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)
///
# Another Method to create sets in Python3
# Set containing numbers
my_set = {1, 2, 3}

print(my_set)
///
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)
////
# Addition of elements to the Set
# using Update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
///
# Creating a set
set1 = set(["Geeks", "For", "Geeks."])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")

# Checking the element
# using in keyword
print("\n")
print("Geeks" in set1)
////
# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set  using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)
////
# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)
/////
#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)


# Removing all the elements from 
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)
///
# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())
////
# Typecasting list into set
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 2]
my_set = set(my_list)
print("my_list as a set: ", my_set)

# Typecasting string into set
my_str = "GeeksforGeeks"
my_set1 = set(my_str)
print("my_str as a set: ", my_set1)

# Typecasting dictionary into set
my_dict = {1: "One", 2: "Two", 3: "Three"}
my_set2 = set(my_dict)
print("my_dict as a set: ", my_set2)
////
def create_set():
    my_set = {1, 2, 3, 4, 5}
    print(my_set)


def add_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    print(my_set)


def remove_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.remove(3)
    print(my_set)


def clear_set():
    my_set = {1, 2, 3, 4, 5}
    my_set.clear()
    print(my_set)


def set_union():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    my_set = set1.union(set2)
    print(my_set)


def set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.intersection(set2)
    print(my_set)


def set_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.difference(set2)
    print(my_set)


def set_symmetric_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.symmetric_difference(set2)
    print(my_set)


def set_subset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    subset = set2.issubset(set1)
    print(subset)


def set_superset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    superset = set1.issuperset(set2)
    print(superset)


if __name__ == '__main__':
    create_set()
    add_element()
    remove_element()
    clear_set()
    set_union()
    set_intersection()
    set_difference()
    set_symmetric_difference()
    set_subset()
    set_superset()
////

