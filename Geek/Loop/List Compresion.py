numbers = [12, 13, 14,] 
doubled = [x *2  for x in numbers] 
print(doubled)
////
numbers = [1, 2, 3, 4, 5] 
squared = [x ** 2 for x in numbers] 
print(squared)
////
# Using list comprehension to iterate through loop 
List = [character for character in [1, 2, 3]] 
  
# Displaying list 
print(List)
////
list = [i for i in range(11) if i % 2 == 0] 
print(list)
////
matrix = [[j for j in range(3)] for i in range(3)] 
    
print(matrix)
////
# Empty list 
List = [] 
  
# Traditional approach of iterating 
for character in 'Geeks 4 Geeks!': 
    List.append(character) 
  
# Display list 
print(List) 
////
# Using list comprehension to iterate through loop 
List = [character for character in 'Geeks 4 Geeks!'] 
  
# Displaying list 
print(List) 
////
# Import required module 
import time 
  
  
# define function to implement for loop 
def for_loop(n): 
    result = [] 
    for i in range(n): 
        result.append(i**2) 
    return result 
  
  
# define function to implement list comprehension 
def list_comprehension(n): 
    return [i**2 for i in range(n)] 
  
  
# Driver Code 
  
# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 
  
# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 
  
# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 
  
# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2))
////
matrix = [] 
  
for i in range(3): 
  
    # Append an empty sublist inside the list 
    matrix.append([]) 
  
    for j in range(5): 
        matrix[i].append(j) 
  
print(matrix) 
////
# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(3)] 
  
print(matrix) 
////
# using lambda to print table of 10  
numbers = [] 
  
for i in range(1, 6): 
    numbers.append(i*10) 
  
print(numbers)
////
numbers = [i*10 for i in range(1, 6)] 
  
print(numbers) 
////
# using lambda to print table of 10 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 
  
print(numbers) 
////
lis = ["Even number" if i % 2 == 0 
       else "Odd number" for i in range(8)] 
print(lis) 
////
lis = [num for num in range(100)  
       if num % 5 == 0 if num % 10 == 0] 
print(lis)
////
# Getting square of number from 1 to 10 
squares = [n**2 for n in range(1, 11)] 
  
# Display square of even numbers 
print(squares) 
////
# Assign matrix 
twoDMatrix = [[10, 20, 30], 
              [40, 50, 60], 
              [70, 80, 90]] 
  
# Generate transpose 
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))] 
  
print(trans) 
////
# Initializing string 
string = 'Geeks4Geeks'
  
# Toggle case of each character 
List = list(map(lambda i: chr(ord(i) ^ 32), string)) 
  
# Display list 
print(List) 
////
# Reverse each string in tuple 
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')] 
  
# Display list 
print(List) 
////
names = ["G", "G", "g"] 
ages = [25, 30, 35] 
person_tuples = [(name, age) for name, age in zip(names, ages)] 
print(person_tuples)
////
# Explicit function 
def digitSum(n): 
    dsum = 0
    for ele in str(n): 
        dsum += int(ele) 
    return dsum 
  
  
# Initializing list 
List = [367, 111, 562, 945, 6726, 873] 
  
# Using the function on odd elements of the list 
newList = [digitSum(i) for i in List if i & 1] 
  
# Displaying new list 
print(newList)
////
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
cube = [number**3 for number in numbers] 
print(cube)
////
words = ["apple", "banana", "cherry", "orange"] 
word_lengths = [len(word) for word in words] 
print(word_lengths)
////

