# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
////
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
////
# Define a function to check 
# if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0


# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result)
////
# Example using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = [num for num in numbers if num % 2 == 0]
print(filtered_numbers)  # Output: [2, 4, 6, 8]
////
# Example using filter() with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)  # Output: [2, 4, 6, 8]
////
# Example filtering objects based on attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 22)
]
# Filter people older than 25
filtered_people = list(filter(lambda person: person.age > 25, people))
for person in filtered_people:
    print(person.name, person.age)
/////
# Example filtering text using list comprehension
text = "Python is awesome and versatile"
filtered_words = [word for word in text.split() if 'o' in word]
print(filtered_words)  # Output: ['Python', 'awesome']
////

