# Python program explaining
# packbits() function
import numpy as np

# creating an array using 
# array function
a = np.array([[[1,0,1],
             [0,1,0]],
             [[1,1,0],
             [0,0,1]]])

# packing elements of an array
# using packbits() function
b = np.packbits(a, axis=-1)

print(b)
# Python program explaining
# unpackbits() function
import numpy as np

# creating an array using 
# array function
a = np.array([[2], [7], [23]], dtype=np.uint8)

# packing elements of an array
# using packbits() function
b = np.unpackbits(a, axis = 1)

print(b)

# Python program explaining
# sin() function
 
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
Sin_Values = np.sin(in_array)
print ("\nSine values : \n", Sin_Values)
# Python program explaining
# cos() function
 
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
cos_Values = np.cos(in_array)
print ("\nCosine values : \n", cos_Values)
 
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
Sinh_Values = np.sinh(in_array)
print ("\nSine Hyperbolic values : \n", Sinh_Values)
# Python3 program explaining
# cosh() function
 
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
cosh_Values = np.cosh(in_array)
print ("\ncosine Hyperbolic values : \n", cosh_Values)
# Python program explaining
# around() function
 
import numpy as np
 
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)
 
round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)
 
 
in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)
 
round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)
 
in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)
 
round_off_values = np.around(in_array, decimals = 3)
print ("\nRounded values : \n", round_off_values)
# Python program explaining
# round_() function
import numpy as np
 
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)
 
round_off_values = np.round_(in_array)
print ("\nRounded values : \n", round_off_values)
 
 
in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)
 
round_off_values = np.round_(in_array)
print ("\nRounded values : \n", round_off_values)
 
in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)
 
round_off_values = np.round_(in_array, decimals = 3)
print ("\nRounded values : \n", round_off_values)
# Python program explaining
# exp() function
import numpy as np
 
in_array = [1, 3, 5]
print ("Input array : ", in_array)
 
out_array = np.exp(in_array)
print ("Output array : ", out_array)
# Python program explaining
# log() function
import numpy as np
 
in_array = [1, 3, 5, 2**8]
print ("Input array : ", in_array)
 
out_array = np.log(in_array)
print ("Output array : ", out_array)
 
 
print("\nnp.log(4**4) : ", np.log(4**4))
print("np.log(2**8) : ", np.log(2**8))
# Python3 code demonstrate reciprocal() function
 
# importing numpy
import numpy as np
 
in_num = 2.0
print ("Input  number : ", in_num)
 
out_num = np.reciprocal(in_num)
print ("Output number : ", out_num)
# Python program explaining
# divide() function
import numpy as np
 
# input_array
arr1 = [2, 27, 2, 21, 23]
arr2 = [2, 3, 4, 5, 6]
print ("arr1         : ", arr1)
print ("arr2         : ", arr2)
 
# output_array
out = np.divide(arr1, arr2)
print ("\nOutput array : \n", out)
# Python Program illustrating
# numpy.isreal() method
  
import numpy as geek 
 
print("Is Real : ", geek.isreal([1+1j, 0j]), "\n")
 
print("Is Real : ", geek.isreal([1, 0]), "\n")
# Python3 code demonstrate conj() function
 
#importing numpy
import numpy as np
 
in_complx1 = 2+4j
out_complx1 = np.conj(in_complx1)
print ("Output conjugated complex number of  2+4j : ", out_complx1)
 
in_complx2 =5-8j
out_complx2 = np.conj(in_complx2)
print ("Output conjugated complex number of 5-8j: ", out_complx2)
# Python program explaining
# cbrt () function
  
import numpy as np
  
arr1 = [1, 27000, 64, -1000]
print ("cbrt Value of arr1 : \n", np.cbrt(arr1))
  
arr2 = [1024 ,-128]
print ("\ncbrt Value of arr2 : ", np.cbrt(arr2))
# Python3 code demonstrate clip() function
 
# importing the numpy
import numpy as np
 
in_array = [1, 2, 3, 4, 5, 6, 7, 8 ]
print ("Input array : ", in_array)
 
out_array = np.clip(in_array, a_min = 2, a_max = 6)
print ("Output array : ", out_array)


import numpy as np
 
# converting to lowercase
print(np.char.lower(['GEEKS', 'FOR']))
 
# converting to lowercase
print(np.char.lower('GEEKS'))
import numpy as np
 
# splitting a string
print(np.char.split('geeks for geeks'))
 
# splitting a string
print(np.char.split('geeks, for, geeks', sep = ','))

import numpy as np
 
# splitting a string
print(np.char.join('-', 'geeks'))
 
# splitting a string
print(np.char.join(['-', ':'], ['geeks', 'for']))
import numpy as np
 
a=np.array(['geeks', 'for', 'geeks'])
 
# counting a substring
print(np.char.count(a,'geek'))
 
# counting a substring
print(np.char.count(a, 'fo'))
import numpy as np
 
a=np.array(['geeks', 'for', 'geeks'])
 
# counting a substring
print(np.char.rfind(a,'geek'))
 
# counting a substring
print(np.char.rfind(a, 'fo'))
import numpy as np
 
# counting a substring
print(np.char.isnumeric('geeks'))
 
# counting a substring
print(np.char.isnumeric('12geeks'))
import numpy as np
 
# using equal() method
a=np.char.equal('geeks','for')
 
print(a)
import numpy as np

# Comparing a string element-wise using not_equal() method
a = np.char.not_equal('geeks', 'for')

print(a)
import numpy as np
 
# comparing a string elementwise
a=np.char.greater('geeks','for')
 
print(a)
import numpy as np
arr = np.array([1, 2, 3, 4])  # Creating a NumPy array
print(arr)  
import numpy as np
char_arr = np.chararray((2, 3))  # Creating a 2x3 character array
char_arr[:] = 'Hello'  # Assigning string values
print(char_arr)  
import numpy as np
lst = [1, 2, 3, 4]
arr = np.asarray(lst)  # Converting list to NumPy array
print(arr)  


import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
scalar = 10  # Scalar value

result = array_2d + scalar
print(result)
import numpy as np
arr = np.array([1, 2, 3])

res = arr + 1  # Adds 1 to each element
print(res)
import numpy as np

# Broadcasting a 1D array with a 2D array
a1 = np.array([2, 4, 6])
a2 = np.array([[1, 3, 5], [7, 9, 11]])
res = a1 + a2
print(res)
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
result = matrix * vector
print(result)
import numpy as np
food_data = np.array([[0.8, 2.9, 3.9], 
                      [52.4, 23.6, 36.5],
                      [55.2, 31.7, 23.9],
                      [14.4, 11, 4.9]])
# Caloric values per gram
caloric_values = np.array([3, 3, 8]) 
# Broadcast caloric values to match food data
caloric_matrix = caloric_values 

# Calculate calorie breakdown for each food
calorie_breakdown = food_data * caloric_matrix
print(calorie_breakdown)
import numpy as np

temperatures = np.array([
    [30, 32, 34, 33, 31],  
    [25, 27, 29, 28, 26], 
    [20, 22, 24, 23, 21]  
])

# Correction factors for each city
corrections = np.array([1.5, -0.5, 2.0])

adjusted_temperatures = temperatures + corrections[:, np.newaxis]
print(adjusted_temperatures)
import numpy as np

# Example image data (3x3 grayscale image)
image = np.array([
    [100, 120, 130],
    [90, 110, 140],
    [80, 100, 120]
])

mean = image.mean(axis=0)   # Mean per column (feature-wise)
std = image.std(axis=0)     # Standard deviation per column

# Normalize using broadcasting
normalized_image = (image - mean) / std
print(normalized_image)
import numpy as np

data = np.array([
    [10, 20],
    [15, 25],
    [20, 30]
])

feature_mean = data.mean(axis=0)
# Center data using broadcasting
centered_data = data - feature_mean
print(centered_data)
#Slicing e Indexing
import numpy as np
# Create a sequence of integers from 10 to 1 with a step of -2
a = np.arange(10, 1, -2) 
print("\n A sequential array with a negative step: \n",a)
# Indexes are specified inside the np.array method.
newarr = a[np.array([3, 1, 2 ])]
print("\n Elements at these indices are:\n",newarr)
import numpy as np 
# Arrange elements from 0 to 19 
a = np.arrange(20) 
print("\n Array is:\n ",a) 
print("\n a[15]=",a[15])
# a[start:stop:step]
print("\n a[-8:17:1] = ",a[-8:17:1]) 
print("\n a[10:] = ",a[10:]) 

import numpy as np 
# A 3 dimensional array. 
b = np.array([[[1, 2, 3],[4, 5, 6]], 
            [[7, 8, 9],[10, 11, 12]]]) 
print(b[...,1]) #Equivalent to b[: ,: ,1 ] 
# Python program showing advanced indexing
import numpy as np
a = np.array([[1 ,2 ],[3 ,4 ],[5 ,6 ]])
print(a[[0 ,1 ,2 ],[0 ,0 ,1]])
# You may wish to select numbers greater than 50
import numpy as np

a = np.array([10, 40, 80, 50, 100])
print(a[a>50])
# You may wish to select those elements whose
# sum of row is a multiple of 10.
import numpy as np

b = np.array([[5, 5],[4, 5],[16, 4]])
sumrow = b.sum(-1)
print(b[sumrow%10==0])

import numpy as np

# Create a 1D NumPy array with five elements
arr = np.array([10, 20, 30, 40, 50])

# Access and print the first element of the array
print(arr[0]) 
import numpy as np 

# Define a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access the element at row 1, column 2 
print(matrix[1, 2]) 
import numpy as np

cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

# Access the element at depth 1, row 2, column 0
print(cube[1, 2, 0]) 
import numpy as np

# Create a 1D NumPy array with six elements
arr = np.array([0, 1, 2, 3, 4, 5])

# Use slicing to access a subset of the array
print(arr[1:4])  
import numpy as np

# Create a 2D NumPy array (matrix) with three rows and three columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use slicing to extract a submatrix
print(matrix[0:2, 1:3]) 
import numpy as np

# Create a 1D NumPy array with five elements
arr = np.array([10, 15, 20, 25, 30])

# Use boolean indexing to filter elements greater than 20
print(arr[arr > 20]) 
import numpy as np 

# Create a 1D NumPy array with five elements
arr = np.array([10, 15, 20, 25, 30])

# Use boolean indexing with multiple conditions to filter elements
print(arr[(arr > 10) & (arr < 30)])  
import numpy as np

cube = np.random.rand(4, 4, 4)

# Selects the first "slice" along the last axis
print(cube[..., 0])  
import numpy as np

# Create a 1D NumPy array with three elements
arr = np.array([1, 2, 3])

# Add a new axis to convert the 1D array into a 2D column vector
# arr[:, np.newaxis] inserts a new axis along the second dimension 
print(arr[:, np.newaxis])  
import numpy as np 

# Create a 1D NumPy array with four elements
arr = np.array([1, 2, 3, 4])

# Modify elements in the array using slicing
arr[1:3] = 99

# Print the updated array to see the changes
print(arr) 
# Importing Numpy module 
import numpy as np 
  
# Creating a 3X3 2-D Numpy array 
arr = np.array([[10, 20, 30],  
                [40, 5, 66],  
                [70, 88, 94]]) 
  
print("Given Array :") 
print(arr) 
  
# Access the First and Last rows of array 
res_arr = arr[[0,2]] 
print("\nAccessed Rows :") 
print(res_arr)
# Importing Numpy module 
import numpy as np 
  
# Creating a 3X4 2-D Numpy array 
arr = np.array([[101, 20, 3, 10],  
                [40, 5, 66, 7],  
                [70, 88, 9, 141]]) 
                 
print("Given Array :") 
print(arr) 
  
# Access the Middle row of array 
res_arr = arr[1] 
print("\nAccessed Row :") 
print(res_arr)
# Importing Numpy module 
import numpy as np 
  
# Creating a 4X4 2-D Numpy array 
arr = np.array([[1, 20, 3, 1],  
                [40, 5, 66, 7],  
                [70, 88, 9, 11], 
               [80, 100, 50, 77]]) 
  
print("Given Array :") 
print(arr) 
  
# Access the Last three rows of array 
res_arr = arr[[1,2,3]] 
print("\nAccessed Rows :") 
print(res_arr)
# Importing Numpy module 
import numpy as np 
  
# Creating a 5X4 2-D Numpy array 
arr = np.array([[1, 20, 3, 1],  
                [40, 5, 66, 7],  
                [70, 88, 9, 11], 
               [80, 100, 50, 77], 
               [1, 8.5, 7.9, 4.8]]) 
  
print("Given Array :") 
print(arr) 
  
# Access the First two rows of array 
res_arr = arr[[0,1]] 
print("\nAccessed Rows :") 
print(res_arr)
# Importing Numpy module  
import numpy as np 
  
# Creating 3-D Numpy array 
n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]],  
                  [[50, 65, 8], [70, 85, 10], [11, 22, 33]]]) 
  
print("Given 3-D Array:") 
print(n_arr) 
  
# Access the Middle rows of 3-D array 
res_arr = n_arr[:,[1]] 
print("\nAccessed Rows :") 
print(res_arr)
# Importing Numpy module  
import numpy as np 
  
# Creating 3-D Numpy array 
n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]],  
                  [[50, 65, 8], [70, 85, 10], [11, 22, 33]], 
                 [[19, 69, 36], [1, 5, 24], [4, 20, 96]]]) 
  
  
print("Given 3-D Array:") 
print(n_arr) 
  
# Access the First and Last rows of 3-D array 
res_arr = n_arr[:,[0, 2]] 
print("\nAccessed Rows :") 
print(res_arr)

# shaping
import numpy as npy
 
# creating a 2-d array
arr1 = npy.array([[1, 3, 5, 7], [2, 4, 6, 8]])
 
# creating a 3-d array
arr2 = npy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
 
print(arr1.shape)
print(arr2.shape)
import numpy as npy
 
# creating an array of 6 dimension
# using ndim
arr = npy.array([2, 4, 6, 8, 10], ndmin=6)
 
# printing array
print(arr)
 
# verifying the value of last dimension
# as 5
print('shape of an array :', arr.shape)
import numpy as np
 
# Create an array of tuples
array_of_tuples = np.array([(1, 2), (3, 4), (5, 6), (7, 8)])
 
# Display the array
print("Array of Tuples:")
print(array_of_tuples)
 
# Determine and display the shape
shape = array_of_tuples.shape
print("\nShape of Array:", shape)
# importing numpy
import numpy as np
 
# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
 
# printing array
print("Array : " + str(array))
 
# length of array
n = array.size
 
# N-D array N dimension
N = 4
 
# calculating M
M = n//N
 
# reshaping numpy array
# converting it to 2-D from 1-D array
reshaped1 = array.reshape((N, M))
 
# printing reshaped array
print("First Reshaped Array : ")
print(reshaped1)
 
# creating another reshaped array
reshaped2 = np.reshape(array, (2, 8))
 
# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped2)
# importing numpy
import numpy as np
 
# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
 
# printing array
print("Array : " + str(array))
 
 
# reshaping numpy array
# converting it to 3-D from 1-D array
reshaped = array.reshape((2, 2, 4))
 
# printing reshaped array
print("Reshaped 3-D Array : ")
print(reshaped)
# importing numpy
import numpy as np
 
# creating a numpy array
array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
 
# printing array
print(" 2-D Array : ")
print(array)
 
 
# reshaping numpy array
# converting it to 1-D from 2-D array
reshaped = array.reshape((9))
 
# or we can use unknown dimension
# reshaped = array.reshape((-1))
 
# printing reshaped array
print("Reshaped 1-D Array : ")
print(reshaped)
# importing numpy
import numpy as np
 
# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
 
# printing array
print("Array : " + str(array))
 
 
# reshaping numpy array
# converting it to 3-D from 1-D array
reshaped1 = array.reshape((2, 2, -1))
 
# printing reshaped array
print("First Reshaped Array : ")
print(reshaped1)
 
 
# converting it to 2-D array
reshaped2 = array.reshape((4, -1))
 
# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped2)
# importing numpy
import numpy as np
 
# creating a numpy array
array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
 
# printing array
print(" 2-D Array : ")
print(array)
 
 
# reshaping numpy array
# converting it to 1-D from 2-D array
# reshaping it into 1, 5
reshaped = array.reshape((1, 5))
 
# or we can use 
 
# printing reshaped array
print("Reshaped 1-D Array : ")
print(reshaped)
# importing numpy as geek 
import numpy as geek
 
arr = geek.array([[5, 6], [7, 8]])
 
gfg = arr.flatten()
 
print( gfg )
# importing numpy as geek 
import numpy as geek
 
arr = geek.array([[5, 6], [7, 8]])
 
gfg = arr.flatten('F')
 
print( gfg )
import numpy as np
 
# Create two 2D arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
 
# Flatten the arrays and concatenate them
concatenated_array = np.concatenate((array1.flatten(), array2.flatten()))
 
print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nConcatenated Array:")
print(concatenated_array)
import numpy as np
 
# Create a 2D array
original_array = np.array([[1, 2, 3],
                           [4, 5, 6]])
 
# Flatten the array and initialize a new flattened array with zeros
flattened_zeros = np.zeros_like(original_array.flatten())
 
print("Original Array:")
print(original_array)
print("\nFlattened Zeros Array:")
print(flattened_zeros)
import numpy as np
 
# Create a 3x3 array
original_array = np.array([[4, 12, 8],
                           [5, 9, 10],
                           [7, 6, 11]])
 
# Flatten the array and find the maximum value
max_value = original_array.flatten().max()
 
print("Original Array:")
print(original_array)
print("\nMaximum Value in Flattened Array:", max_value)
#sorting
# importing libraries 
import numpy as np 
  
a = np.array([12, 15, 10, 1]) 
print("Array before sorting",a) 
a.sort() 
print("Array after sorting",a) 
# importing libraries 
import numpy as np 
# sort along the first axis 
a = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(a, axis = 0)         
print ("Along first axis : \n", arr1)         
# sort along the last axis 
a = np.array([[10, 15], [12, 1]]) 
arr2 = np.sort(a, axis = -1)         
print ("\nAlong first axis : \n", arr2) 
a = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(a, axis = None)         
print ("\nAlong none axis : \n", arr1)
import numpy as np 
  
# Numpy array created 
a = np.array([9, 3, 1, 7, 4, 3, 6]) 
  
# unsorted array print 
print('Original array:\n', a) 
  
# Sort array indices 
b = np.argsort(a) 
print('Sorted indices of original array->', b) 
  
# To get sorted array using sorted indices 
# c is temp array created of same len as of b 
c = np.zeros(len(b), dtype = int) 
for i in range(0, len(b)): 
    c[i]= a[b[i]] 
print('Sorted array->', c) 
import numpy as np 
  
# Numpy array created 
# First column 
a = np.array([9, 3, 1, 3, 4, 3, 6]) 
  
# Second column 
b = np.array([4, 6, 9, 2, 1, 8, 7]) 
print('column a, column b') 
for (i, j) in zip(a, b): 
    print(i, ' ', j) 
  
# Sort by a then by b 
ind = np.lexsort((b, a)) 
print('Sorted indices->', ind) 
# Python code to sort an array in-place 
# using a.sort 
import numpy as np 
  
# Numpy array created 
a = np.array([9, 3, 1, 7, 4, 3, 6]) 
  
# unsorted array print 
print('Original array:\n', a) 
  
# Return type is None 
print('Return type:', a.sort()) 
  
# Sorted array output 
print('Original array sorted->', a) 
# Python code to create a sorted copy using 
# sorted() 
import numpy as np 
  
# Numpy array created 
a = np.array([9, 3, 1, 7, 4, 3, 6]) 
  
# unsorted array print 
print('Original array:\n', a) 
b = sorted(a) 
  
# sorted list returned to b, b type is 
# <class 'list'>  
print('New array sorted->', b) 
  
# original array no change 
print('Original array->', a) 
# Python code to demonstrate working of np.argsort 
import numpy as np 
  
# Numpy array created 
a = np.array([9, 3, 1, 7, 4, 3, 6]) 
  
# unsorted array print 
print('Original array:\n', a) 
  
# Sort array indices 
b = np.argsort(a) 
print('Sorted indices of original array->', b) 
  
# To get sorted array using sorted indices 
# c is temp array created of same len as of b 
c = np.zeros(len(b), dtype = int) 
for i in range(0, len(b)): 
    c[i]= a[b[i]] 
print('Sorted array->', c) 
# Python code to demonstrate working of  
# np.lexsort() 
import numpy as np 
  
# Numpy array created 
a = np.array([9, 3, 1, 3, 4, 3, 6]) # First column 
b = np.array([4, 6, 9, 2, 1, 8, 7]) # Second column 
print('column a, column b') 
for (i, j) in zip(a, b): 
    print(i, ' ', j) 
  
ind = np.lexsort((b, a)) # Sort by a then by b 
print('Sorted indices->', ind) 
# importing the module 
import numpy as np 
  
# creating the array 
arr = np.array([10, 32, 30, 50, 20, 82, 91, 45]) 
  
#  printing arr 
print("arr = {}".format(arr)) 
  
#  looking for value 30 in arr and storing its index in i 
i = np.where(arr == 30) 
print("i = {}".format(i))
# importing the module 
import numpy as np 
  
# creating the array 
arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6] 
print("arr = {}".format(arr)) 
  
# left-most 3 
print("left-most index = {}".format(np.searchsorted(arr, 3, side="left"))) 
  
# right-most 3 
print("right-most index = {}".format(np.searchsorted(arr, 3, side="right")))
# importing libraries
import numpy as np
 
# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)        
print ("Along first axis : \n", arr1)        
 
 
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis = -1)        
print ("\nAlong first axis : \n", arr2)
 
 
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)        
print ("\nAlong none axis : \n", arr1)
# Python code to demonstrate 
# working of  numpy.argsort
import numpy as np
 
# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])
 
# unsorted array print
print('Original array:\n', a)
 
# Sort array indices
b = np.argsort(a)
print('Sorted indices of original array->', b)
 
# To get sorted array using sorted indices
# c is temp array created of same len as of b
c = np.zeros(len(b), dtype = int)
for i in range(0, len(b)):
    c[i]= a[b[i]]
print('Sorted array->', c)
# Python code to demonstrate working of 
# numpy.lexsort()
import numpy as np
 
# Numpy array created
# First column
a = np.array([9, 3, 1, 3, 4, 3, 6])
 
# Second column 
b = np.array([4, 6, 9, 2, 1, 8, 7]) 
print('column a, column b')
for (i, j) in zip(a, b):
    print(i, ' ', j)
 
# Sort by a then by b
ind = np.lexsort((b, a)) 
print('Sorted indices->', ind)
# Python Program illustrating
# working of argmax()
 
import numpy as geek 
 
# Working on 2D array
array = geek.arange(12).reshape(3, 4)
print("INPUT ARRAY : \n", array)
 
# No axis mentioned, so works on entire array
print("\nMax element : ", geek.argmax(array))
 
# returning Indices of the max element
# as per the indices
print(("\nIndices of Max element : "
      , geek.argmax(array, axis=0)))
print(("\nIndices of Max element : "
      , geek.argmax(array, axis=1)))
# Python Program illustrating
# working of nanargmax()
 
import numpy as geek 
 
# Working on 1D array
array = [geek.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)
 
array2 = geek.array([[geek.nan, 4], [1, 3]])
 
# returning Indices of the max element
# as per the indices ingnoring NaN
print(("\nIndices of max in array1 : "
       , geek.nanargmax(array)))
 
# Working on 2D array
print("\nINPUT ARRAY 2 : \n", array2)
print(("\nIndices of max in array2 : "
      , geek.nanargmax(array2)))
 
print(("\nIndices at axis 1 of array2 : "
      , geek.nanargmax(array2, axis = 1)))
# Python Program illustrating
# working of argmin()
 
import numpy as geek 
 
# Working on 1D array
array = geek.arange(8)
print("INPUT ARRAY : \n", array)
 
 
# returning Indices of the min element
# as per the indices
print("\nIndices of min element : ", geek.argmin(array, axis=0))
import numpy as np

# Counting the number of non-zero values in the entire array
a = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])

# Counting the number of non-zero values along axis 0 (column-wise)
b = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=0)

print("Number of nonzero values in the entire array is:", a)
print("Number of nonzero values along axis 0 is:", b)
#Combine
import numpy as np 
  
array_1 = np.array([1, 2]) 
array_2 = np.array([3, 4]) 
  
array_new = np.concatenate((array_1, array_2)) 
print(array_new) 
#join
# Python program explaining 
# hstack() function 
  
import numpy as geek 
  
# input array 
in_arr1 = geek.array([ 1, 2, 3] ) 
print ("1st Input array : \n", in_arr1)  
  
in_arr2 = geek.array([ 4, 5, 6] ) 
print ("2nd Input array : \n", in_arr2)  
  
# Stacking the two arrays horizontally 
out_arr = geek.hstack((in_arr1, in_arr2)) 
print ("Output horizontally stacked array:\n ", out_arr) 
# Python program explaining 
# hstack() function 
  
import numpy as geek 
  
# input array 
in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2, -3]] ) 
print ("1st Input array : \n", in_arr1)  
  
in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5, -6]] ) 
print ("2nd Input array : \n", in_arr2)  
  
# Stacking the two arrays horizontally 
out_arr = geek.hstack((in_arr1, in_arr2)) 
print ("Output stacked array :\n ", out_arr) 
# Python program explaining 
# vstack() function 
  
import numpy as geek 
  
# input array 
in_arr1 = geek.array([ 1, 2, 3] ) 
print ("1st Input array : \n", in_arr1)  
  
in_arr2 = geek.array([ 4, 5, 6] ) 
print ("2nd Input array : \n", in_arr2)  
  
# Stacking the two arrays vertically 
out_arr = geek.vstack((in_arr1, in_arr2)) 
print ("Output vertically stacked array:\n ", out_arr) 
# Python program explaining 
# vstack() function 
  
import numpy as geek 
  
# input array 
in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2, -3]] ) 
print ("1st Input array : \n", in_arr1)  
  
in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5, -6]] ) 
print ("2nd Input array : \n", in_arr2)  
  
# Stacking the two arrays vertically 
out_arr = geek.vstack((in_arr1, in_arr2)) 
print ("Output stacked array :\n ", out_arr) 
import numpy as np 
  
array_1 = np.array([1, 2]) 
array_2 = np.array([3, 4]) 
  
array_new = np.concatenate((array_1, array_2)) 
print(array_new) 
import numpy as np 
  
array_1 = np.array([[1, 2], [3, 4]]) 
array_2 = np.array([[5, 6], [7, 8]]) 
  
array_new = np.concatenate((array_1, array_2), axis=1) 
print(array_new) 
import numpy as np 
  
array_1 = np.array([1, 2, 3, 4]) 
array_2 = np.array([5, 6, 7, 8]) 
  
array_new = np.stack((array_1, array_2), axis=1) 
print(array_new) 
import numpy as np 
  
block_1 = np.array([[1, 1], [1, 1]]) 
block_2 = np.array([[2, 2, 2], [2, 2, 2]]) 
block_3 = np.array([[3, 3], [3, 3], [3, 3]]) 
block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]]) 
  
block_new = np.block([ 
    [block_1, block_2], 
    [block_3, block_4] 
]) 
  
print(block_new) 
# importing Numpy package  
import numpy as np 
  
num_1d = np.arange(5) 
print("One dimensional array:") 
print(num_1d) 
  
num_2d = np.arange(10).reshape(2,5) 
print("\nTwo dimensional array:") 
print(num_2d) 
  
# Combine 1-D and 2-D arrays and display  
# their elements using numpy.nditer()  
for a, b in np.nditer([num_1d, num_2d]): 
    print("%d:%d" % (a, b),)
# importing Numpy package  
import numpy as np 
  
num_1d = np.arange(7) 
print("One dimensional array:") 
print(num_1d) 
  
num_2d = np.arange(21).reshape(3,7) 
print("\nTwo dimensional array:") 
print(num_2d) 
  
# Combine 1-D and 2-D arrays and display  
# their elements using numpy.nditer()  
for a, b in np.nditer([num_1d, num_2d]): 
    print("%d:%d" % (a, b),)
# importing Numpy package  
import numpy as np 
  
num_1d = np.arange(2) 
print("One dimensional array:") 
print(num_1d) 
  
num_2d = np.arange(12).reshape(6,2) 
print("\nTwo dimensional array:") 
print(num_2d) 
  
# Combine 1-D and 2-D arrays and display 
# their elements using numpy.nditer()  
for a, b in np.nditer([num_1d, num_2d]): 
    print("%d:%d" % (a, b),)
import numpy as np
Arr = np.array([1, 2, 3, 4, 5, 6])
array = np.array_split(arr, 3)
print(array)
import numpy as np
 
# Creating an example array
array = np.arange(6)
 
# Splitting the array into 2 equal parts along the first axis (axis=0)
result = np.split(array, 2)
 
print("Array:")
print(array)
print("\nResult after numpy.split():")
print(result)
import numpy as np
 
# Creating an example array
array = np.arange(13)
 
# Splitting the array into 4 unequal parts along the first axis (axis=0)
result = np.array_split(array, 4)
 
print("Array:")
print(array)
print("\nResult after numpy.array_split():")
print(result)
import numpy as np
 
# Creating a 2D array
array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
 
# Splitting the array into 3 equal parts along the second axis (axis=1)
result = np.split(array, 3, axis=1)
 
print("2D Array:")
print(original_array)
print("\nResult after numpy.split() along axis=1:")
print(result)
import numpy as np
 
# Creating an example matrix
matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]])
 
# Vertical splitting into 2 subarrays along axis=0
result = np.vsplit(matrix, 2)
 
print("Matrix:")
print(matrix)
print("\nResult after numpy.vsplit():")
print(result)
import numpy as np
 
# Creating an example 2D array
array = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])
 
# Horizontal splitting into 2 subarrays along axis=1
result = np.hsplit(array, 2)
 
print("2D Array:")
print(array)
print("\nResult after numpy.hsplit():")
print(result)
import numpy as np
 
# Creating an example 3D array
original_3d_array = np.arange(24).reshape((2, 3, 4))
 
# Splitting along axis=2 (third axis)
result = np.dsplit(original_3d_array, 2)
 
print("Original 3D Array:")
print(original_3d_array)
print("\nResult after numpy.dsplit():")
print(result)

# Python Program illustrating 
# numpy.sum() method
import numpy as np 
    
# 1D array 
arr = [20, 2, .2, 10, 4] 

print("\nSum of arr : ", np.sum(arr)) 

print("Sum of arr(uint8) : ", np.sum(arr, dtype = np.uint8)) 
print("Sum of arr(float32) : ", np.sum(arr, dtype = np.float32))

print ("\nIs np.sum(arr).dtype == np.uint : ", 
    np.sum(arr).dtype == np.uint) 

print ("Is np.sum(arr).dtype == np.float : ", 
    np.sum(arr).dtype == np.float) 
# Python Program illustrating 
# numpy.sum() method
import numpy as np 
    
# 2D array 
arr = [[14, 17, 12, 33, 44], 
    [15, 6, 27, 8, 19], 
    [23, 2, 54, 1, 4,]] 

print("\nSum of arr : ", np.sum(arr)) 

print("Sum of arr(uint8) : ", np.sum(arr, dtype = np.uint8)) 
print("Sum of arr(float32) : ", np.sum(arr, dtype = np.float32))

print ("\nIs np.sum(arr).dtype == np.uint : ", 
                np.sum(arr).dtype == np.uint) 

print ("Is np.sum(arr).dtype == np.float : ", 
            np.sum(arr).dtype == np.float) 
# Python Program illustrating 
# numpy.sum() method 
import numpy as np 
    
# 2D array 
arr = [[14, 17, 12, 33, 44], 
    [15, 6, 27, 8, 19], 
    [23, 2, 54, 1, 4,]] 

print("\nSum of arr : ", np.sum(arr)) 
print("Sum of arr(axis = 0) : ", np.sum(arr, axis = 0)) 
print("Sum of arr(axis = 1) : ", np.sum(arr, axis = 1))

print("\nSum of arr (keepdimension is True): \n",
    np.sum(arr, axis = 1, keepdims = True))
# Python Program illustrating  
# numpy.mean() method  
import numpy as np 
    
# 1D array  
arr = [20, 2, 7, 1, 34] 
  
print("arr : ", arr)  
print("mean of arr : ", np.mean(arr)) 
# Python Program illustrating  
# numpy.mean() method    
import numpy as np 
    
  
# 2D array  
arr = [[14, 17, 12, 33, 44],   
       [15, 6, 27, 8, 19],  
       [23, 2, 54, 1, 4, ]]  
    
# mean of the flattened array  
print("\nmean of arr, axis = None : ", np.mean(arr))  
    
# mean along the axis = 0  
print("\nmean of arr, axis = 0 : ", np.mean(arr, axis = 0))  
   
# mean along the axis = 1  
print("\nmean of arr, axis = 1 : ", np.mean(arr, axis = 1)) 
  
out_arr = np.arange(3) 
print("\nout_arr : ", out_arr)  
print("mean of arr, axis = 1 : ",  
      np.mean(arr, axis = 1, out = out_arr)) 
      
#matrix
# Python code to demonstrate matrix operations 
# add(), subtract() and divide() 

# importing numpy for matrix operations 
import numpy 

# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 

# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 

# using subtract() to subtract matrices 
print ("The element wise subtraction of matrix is : ") 
print (numpy.subtract(x,y)) 

# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (numpy.divide(x,y)) 
# Python code to demonstrate matrix operations 
# multiply() and dot() 

# importing numpy for matrix operations 
import numpy 

# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 

# using multiply() to multiply matrices element wise 
print ("The element wise multiplication of matrix is : ") 
print (numpy.multiply(x,y)) 

# using dot() to multiply matrices 
print ("The product of matrices is : ") 
print (numpy.dot(x,y)) 
# Python code to demonstrate matrix operations 
# sqrt(), sum() and "T" 

# importing numpy for matrix operations 
import numpy 

# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 

# using sqrt() to print the square root of matrix 
print ("The element wise square root is : ") 
print (numpy.sqrt(x)) 

# using sum() to print summation of all elements of matrix 
print ("The summation of all matrix element is : ") 
print (numpy.sum(y)) 

# using sum(axis=0) print summation of each column of matrix 
print ("The column wise summation of all matrix is : ") 
print (numpy.sum(y,axis=0)) 

# using sum(axis=1) print summation of each row of matrix 
print ("The row wise summation of all matrix is : ") 
print (numpy.sum(y,axis=1)) 

# using "T" to transpose the matrix 
print ("The transpose of given matrix is : ") 
print (x.T) 
A = [[1,2],[4,5]] 
B = [[7,8],[9,10]] 
rows = len(A) 
cols = len(A[0]) 

# Element wise addition 
C = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        C[i][j] = A[i][j] + B[i][j] 
print("Addition of matrices: \n", C) 

# Element wise subtraction 
D = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        D[i][j] = A[i][j] - B[i][j] 
print("Subtraction of matrices: \n", D) 

# Element wise division 
E = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        E[i][j] = A[i][j] / B[i][j] 
print("Division of matrices: \n", E) 
import numpy as np
 
# Original matrix
original_matrix = np.matrix([[1, 2, 3], [4, 5, 6]])
 
# Transposed matrix
transposed_matrix = original_matrix.transpose()
 
print("Original Matrix:")
print(original_matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)
# import the important module in python 
import numpy as np 
               
# make matrix with numpy 
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]') 
               
# applying matrix.transpose() method 
geek = gfg.transpose() 
     
print(geek)
import numpy as np
 
# Matrices for multiplication
matrix_a = np.matrix([[1, 2], [3, 4]])
matrix_b = np.matrix([[5, 6], [7, 8]])
 
# Transpose one matrix before multiplication
result = matrix_a * matrix_b.transpose()
 
print("Result of Matrix Multiplication:")
print(result)
# Import required package
import numpy as np
 
# Taking a 3 * 3 matrix
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Calculating the inverse of the matrix
print(np.linalg.inv(A))
# Import required package
import numpy as np
 
# Taking a 4 * 4 matrix
A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
 
# Calculating the inverse of the matrix
print(np.linalg.inv(A))
# Import required package
import numpy as np
 
# Inverses of several matrices can
# be computed at once
A = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])
 
# Calculating the inverse of the matrix
print(np.linalg.inv(A))
# Python program explaining 
# numpy.ndarray.dot() function 
  
# importing numpy as geek  
import numpy as geek 
  
arr1 = geek.eye(3) 
arr = geek.ones((3, 3)) * 3
  
gfg = arr1.dot( arr ) 
  
print( gfg) 
# Python program explaining 
# numpy.ndarray.dot() function 
  
# importing numpy as geek  
import numpy as geek 
  
arr1 = geek.eye(3) 
arr = geek.ones((3, 3)) * 3
  
gfg = arr1.dot(arr).dot(arr) 
  
print( gfg) 
# import the important module in python 
import numpy as np 
              
# make matrix with numpy 
gfg = np.matrix('[4, 1; 12, 3]') 
              
# applying matrix.var() method 
geek = gfg.var() 
    
print(geek) 
# import the important module in python 
import numpy as np 
              
# make matrix with numpy 
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]') 
              
# applying matrix.var() method 
geek = gfg.var() 
    
print(geek) 
#Linear Algebra
# Importing numpy as np
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))
import numpy as np
from numpy import linalg as geek

# Creating an array using array function
a = np.array([[1, -2j], [2j, 5]])

print("Array is:", a)

# Calculating eigenvalues and eigenvectors using eigh() function
c, d = geek.eigh(a)

print("Eigenvalues are:", c)
print("Eigenvectors are:", d)
import numpy as np
from numpy import linalg as geek

# Creating an array using diag function
a = np.diag((1, 2, 3))

print("Array is:", a)

# Calculating eigenvalues and eigenvectors using eig() function
c, d = geek.eig(a)

print("Eigenvalues are:", c)
print("Eigenvectors are:", d)
# Python Program illustrating
# numpy.dot() method
 
import numpy as geek
 
# Scalars
product = geek.dot(5, 4)
print("Dot Product of scalar values  : ", product)
 
# 1D array
vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = geek.dot(vector_a, vector_b)
print("Dot Product  : ", product)
# Python Program illustrating
# numpy.vdot() method
 
import numpy as geek
 
# 1D array
vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = geek.vdot(vector_a, vector_b)
print("Dot Product  : ", product)
# Python Program illustrating
# numpy.linalg.solve() method
 
import numpy as np
 
# Creating an array using array
# function
a = np.array([[1, 2], [3, 4]])
 
# Creating an array using array
# function
b = np.array([8, 18])
 
print(("Solution of linear equations:", 
      np.linalg.solve(a, b)))
# Python Program illustrating
# numpy.linalg.lstsq() method
 
 
import numpy as np
import matplotlib.pyplot as plt
 
# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])
 
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0] 
 
# plotting the line
line = w[0]*x + w[1] # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()
# Python Program illustrating
# numpy.linalg.det() method
 
import numpy as np
 
# creating an array using 
# array method
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
 
print(("\nDeterminant of A:"
     , np.linalg.det(A)))
# Python Program illustrating
# numpy.trace()() method
 
import numpy as np
 
# creating an array using 
# array method
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
 
print("\nTrace of A:", np.trace(A))
# Import numpy package 
import numpy as np 
  
# Create a numpy array  
arr = np.array([[10,22],[13,6]]) 
  
# Find the QR factor of array 
q, r =  np.linalg.qr(arr) 
  
# Print the result 
print("Decomposition of matrix:") 
print( "q=\n", q, "\nr=\n", r)
# Import numpy package 
import numpy as np 
  
# Create a numpy array  
arr = np.array([[0, 1], [1, 0], [1, 1], [2, 2]]) 
  
# Find the QR factor of array 
q, r =  np.linalg.qr(arr) 
  
# Print the result 
print("Decomposition of matrix:") 
print( "q=\n", q, "\nr=\n", r) 
# Import numpy package 
import numpy as np 
  
# Create a numpy array  
arr = np.array([[5, 11, -15], [12, 34, -51], 
                [-24, -43, 92]], dtype=np.int32) 
  
# Find the QR factor of array 
q, r = np.linalg.qr(arr) 
  
# Print the result 
print("Decomposition of matrix:") 
print( "q=\n", q, "\nr=\n", r)
# import numpy 
from numpy import linalg as LA 
  
# using np.eigvals() method 
gfg = LA.eigvals([[1, 2], [3, 4]]) 
  
print(gfg) 
# import numpy 
from numpy import linalg as LA 
  
# using np.eigvals() method 
gfg = LA.eigvals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(gfg) 
#Random
# Python program explaining 
# numpy.random.randint() function 
  
# importing numpy 
import numpy as geek 
  
# output array 
out_arr = geek.random.randint(low = 0, high = 3, size = 5) 
print ("Output 1D Array filled with random integers : ", out_arr)
# Python program explaining 
# numpy.random.randint() function 
  
# importing numpy 
import numpy as geek 
  
  
# output array 
out_arr = geek.random.randint(low = 4, size =(2, 3)) 
print ("Output 2D Array filled with random integers : ", out_arr) 
# Python program explaining 
# numpy.random.randint() function 
  
# importing numpy 
import numpy as geek 
  
# output array 
out_arr = geek.random.randint(2, 10, (2, 3, 4)) 
print ("Output 3D Array filled with random integers : ", out_arr)  
# Python Program illustrating 
# numpy.random.rand() method 
   
import numpy as geek 
   
# 1D Array 
array = geek.random.rand(5) 
print("1D Array filled with random values :", array);
# Python Program illustrating 
# numpy.random.rand() method 
   
import numpy as geek 
   
# 2D Array    
array = geek.random.rand(3, 4) 
print("\n\n2D Array filled with random values : ", array); 
# Python Program illustrating 
# numpy.random.rand() method 
   
import numpy as geek 
   
# 3D Array      
array = geek.random.rand(2, 2 ,2) 
print("\n\n3D Array filled with random values : \n", array); 
# importing module 
import numpy as np 
  
  
# numpy.random.normal() method 
r = np.random.normal(size=5) 
  
# printing numbers 
print(r) 
# importing module 
import numpy as np 
  
  
# numpy.random.normal() method 
random_array = np.random.normal(0.0, 1.0, 5) 
  
# printing 1D array with random numbers 
print("1D Array with random values : \n", random_array) 

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
scalar = 10  # Scalar value

result = array_2d + scalar
print(result)
import numpy as np
arr = np.array([1, 2, 3])

res = arr + 1  # Adds 1 to each element
print(res)
import numpy as np

# Broadcasting a 1D array with a 2D array
a1 = np.array([2, 4, 6])
a2 = np.array([[1, 3, 5], [7, 9, 11]])
res = a1 + a2
print(res)
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
result = matrix * vector
print(result)
import numpy as np
food_data = np.array([[0.8, 2.9, 3.9], 
                      [52.4, 23.6, 36.5],
                      [55.2, 31.7, 23.9],
                      [14.4, 11, 4.9]])
# Caloric values per gram
caloric_values = np.array([3, 3, 8]) 
# Broadcast caloric values to match food data
caloric_matrix = caloric_values 

# Calculate calorie breakdown for each food
calorie_breakdown = food_data * caloric_matrix
print(calorie_breakdown)
import numpy as np

temperatures = np.array([
    [30, 32, 34, 33, 31],  
    [25, 27, 29, 28, 26], 
    [20, 22, 24, 23, 21]  
])

# Correction factors for each city
corrections = np.array([1.5, -0.5, 2.0])

adjusted_temperatures = temperatures + corrections[:, np.newaxis]
print(adjusted_temperatures)
import numpy as np

# Example image data (3x3 grayscale image)
image = np.array([
    [100, 120, 130],
    [90, 110, 140],
    [80, 100, 120]
])

mean = image.mean(axis=0)   # Mean per column (feature-wise)
std = image.std(axis=0)     # Standard deviation per column

# Normalize using broadcasting
normalized_image = (image - mean) / std
print(normalized_image)
import numpy as np

data = np.array([
    [10, 20],
    [15, 25],
    [20, 30]
])

feature_mean = data.mean(axis=0)

# Center data using broadcasting
centered_data = data - feature_mean
print(centered_data)
import numpy as np

a1 = np.array([2,4,6,8,10 ])
number= 2
result = a1 + number
print(result)
import numpy as np
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
result = a1 + a2
print(result)  
import numpy as np
a1 = np.array([1, 2, 3, 4])
result = a1 * 2
print(result)  
import numpy as np
a1 = np.array([10, 20, 30])
result = a1 > 15
print(result)  
import numpy as np
a1= np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
result = np.dot(a1, a2) 
print(result)
import numpy as np

def custom_func(x):
    return x**2 + 2*x + 1

a1 = np.array([1, 2, 3, 4])
result = custom_func(a1)
print(result) 
import numpy as np
a1 = np.array([1, 2, 3])
result_sum = a1.sum()
result_mean = a1.mean()
print(result_sum)   
print(result_mean)  
import numpy as np
import time

start_time = time.time()
vectorized_sum = np.sum(np.arange(15000))
print("Vectorized sum:", vectorized_sum)
print("Time taken by vectorized sum:", time.time() - start_time)

start_time = time.time()
iterative_sum = sum(range(15000)) 
print("\nIterative sum:", iterative_sum)
print("Time taken by iterative sum:", time.time() - start_time)
# Python code to demonstrate trigonometric function 
import numpy as np 
  
# create an array of angles 
angles = np.array([0, 30, 45, 60, 90, 180])  
  
# conversion of degree into radians 
# using deg2rad function 
radians = np.deg2rad(angles) 
  
# sine of angles 
print('Sine of angles in the array:') 
sine_value = np.sin(radians) 
print(np.sin(radians)) 
  
# inverse sine of sine values 
print('Inverse Sine of sine values:') 
print(np.rad2deg(np.arcsin(sine_value))) 
  
# hyperbolic sine of angles 
print('Sine hyperbolic of angles in the array:') 
sineh_value = np.sinh(radians) 
print(np.sinh(radians)) 
  
# inverse sine hyperbolic  
print('Inverse Sine hyperbolic:') 
print(np.sin(sineh_value))  
  
# hypot function demonstration 
base = 4
height = 3
print('hypotenuse of right triangle is:') 
print(np.hypot(base, height)) 
# Python code demonstrate statistical function 
import numpy as np 
  
# construct a weight array 
weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45]) 
  
# minimum and maximum  
print('Minimum and maximum weight of the students: ') 
print(np.amin(weight), np.amax(weight)) 
  
# range of weight i.e. max weight-min weight 
print('Range of the weight of the students: ') 
print(np.ptp(weight)) 
  
# percentile 
print('Weight below which 70 % student fall: ') 
print(np.percentile(weight, 70)) 
   
# mean  
print('Mean weight of the students: ') 
print(np.mean(weight)) 
  
# median  
print('Median weight of the students: ') 
print(np.median(weight)) 
  
# standard deviation  
print('Standard deviation of weight of the students: ') 
print(np.std(weight)) 
  
# variance  
print('Variance of weight of the students: ') 
print(np.var(weight)) 
  
# average  
print('Average weight of the students: ') 
print(np.average(weight)) 
# Python code to demonstrate bitwise-function 
import numpy as np 
  
# construct an array of even and odd numbers 
even = np.array([0, 2, 4, 6, 8, 16, 32]) 
odd = np.array([1, 3, 5, 7, 9, 17, 33]) 
  
# bitwise_and 
print('bitwise_and of two arrays: ') 
print(np.bitwise_and(even, odd)) 
  
# bitwise_or 
print('bitwise_or of two arrays: ') 
print(np.bitwise_or(even, odd)) 
  
# bitwise_xor 
print('bitwise_xor of two arrays: ') 
print(np.bitwise_xor(even, odd)) 
   
# invert or not 
print('inversion of even no. array: ') 
print(np.invert(even)) 
  
# left_shift  
print('left_shift of even no. array: ') 
print(np.left_shift(even, 1)) 
  
# right_shift  
print('right_shift of even no. array: ') 
print(np.right_shift(even, 1)) 

##QE
import numpy as np

# Create an empty array of shape (3, 4)
empty_array = np.empty((3, 4))
print("Empty Array:\n", empty_array)

# Create a full array of shape (3, 3) filled with the value 5
full_array = np.full((3, 3), 5)
print("Full Array:\n", full_array)
import numpy as np

empty_array_2d = np.empty((3, 4))
print(empty_array_2d)
import numpy as np

full_array_2d = np.full((3, 4), 5)
print(full_array_2d)
import numpy as np

# Create a 1D array of zeros with 5 elements
array_1d = np.zeros(5)
print(array_1d)
import numpy as np

# Create a 2D array of zeros (3 rows, 4 columns)
array_2d = np.zeros((3, 4))
print(array_2d)
import numpy as np

# Create an integer zero array
array_int = np.zeros((2, 3), dtype=int)
print(array_int)
import numpy as np

# Create an array with column-major order
array_column_major = np.zeros((2, 3), order='F')
print(array_column_major)
import numpy as np

array = np.ones(5)
print(array) 
import numpy as np

# Create a 2D array of ones (3 rows, 4 columns)
ones_array_2d = np.ones((3, 4))
print(ones_array_2d)
import numpy as np

# Create an integer array of ones with 4 elements
ones_int_array = np.ones(4, dtype=int)
print(ones_int_array)
import numpy as np

# Create a 3D array of ones with shape (2, 3, 4)
ones_array_3d = np.ones((2, 3, 4))
print(ones_array_3d)
# importing package 
import numpy 
  
# create numpy array 
arr = numpy.array([[1, 2, 3, 4, 5], 
                   [6, 7, 8, 9, 10], 
                   [11, 12, 13, 14, 15], 
                   [16, 17, 18, 19, 20] 
                   ]) 
  
# view array 
print(arr) 
  
# check for some lists 
print([1, 2, 3, 4, 5] in arr.tolist()) 
print([16, 17, 20, 19, 18] in arr.tolist()) 
print([3, 2, 5, -4, 5] in arr.tolist()) 
print([11, 12, 13, 14, 15] in arr.tolist()) 
# Importing Numpy module
import numpy as np

# Creating a 2x3 2-D NumPy array
n_arr = np.array([[10.5, 22.5, 3.8],
                  [41, np.nan, np.nan]])

print("Given array:")
print(n_arr)

print("\nRemove all rows containing NaN values:")
cleaned_arr = n_arr[~np.isnan(n_arr).any(axis=1)]
print(cleaned_arr)
# Importing Numpy module 
import numpy as np

# Creating a 3x3 2-D NumPy array
n_arr = np.array([[10.5, 22.5, 3.8], 
                  [23.45, 50, 78.7],
                  [41, np.nan, np.nan]])

print("Given array:")
print(n_arr)

print("\nRemove all rows containing NaN values:")
cleaned_arr = n_arr[~np.isnan(n_arr).any(axis=1)]
print(cleaned_arr)
# Importing Numpy module
import numpy as np

# Creating a 5x4 2-D NumPy array
n_arr = np.array([[10.5, 22.5, 3.8, 5],
                  [23.45, 50, 78.7, 3.5],
                  [41, np.nan, np.nan, 0],
                  [20, 50.20, np.nan, 2.5],
                  [18.8, 50.60, 8.8, 58.6]])

print("Given array:")
print(n_arr)

print("\nRemove all rows containing NaN values:")
cleaned_arr = n_arr[~np.isnan(n_arr).any(axis=1)]
print(cleaned_arr)
# Python program explaining 
# numpy.squeeze function 
  
import numpy as geek 
  
in_arr = geek.array([[[2, 2, 2], [2, 2, 2]]]) 
   
print ("Input array : ", in_arr)  
print("Shape of input array : ", in_arr.shape)   
  
out_arr = geek.squeeze(in_arr)  
  
print ("output squeezed array : ", out_arr) 
print("Shape of output array : ", out_arr.shape)  
# Python program explaining 
# numpy.squeeze function 
import numpy as geek 
in_arr = geek.arange(9).reshape(1, 3, 3)  
  
print ("Input array : ", in_arr)   
out_arr = geek.squeeze(in_arr, axis = 0)  
  
print ("output array : ", out_arr)   
print("The shapes of Input and Output array : ")  
  
print(in_arr.shape, out_arr.shape) 
# Python program explaining 
# numpy.squeeze function 
# when value error occurs 
import numpy as geek 
  
in_arr = geek.arange(9).reshape(1, 3, 3)  
  
print ("Input array : ", in_arr)   
out_arr = geek.squeeze(in_arr, axis = 1)  
  
print ("output array : ", out_arr)   
print("The shapes of Input and Output array : ") 
   
print(in_arr.shape, out_arr.shape) 

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
scalar = 10  # Scalar value

result = array_2d + scalar
print(result)
import numpy as np
arr = np.array([1, 2, 3])

res = arr + 1  # Adds 1 to each element
print(res)
import numpy as np

# Broadcasting a 1D array with a 2D array
a1 = np.array([2, 4, 6])
a2 = np.array([[1, 3, 5], [7, 9, 11]])
res = a1 + a2
print(res)
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
result = matrix * vector
print(result)
import numpy as np
food_data = np.array([[0.8, 2.9, 3.9], 
                      [52.4, 23.6, 36.5],
                      [55.2, 31.7, 23.9],
                      [14.4, 11, 4.9]])
# Caloric values per gram
caloric_values = np.array([3, 3, 8]) 
# Broadcast caloric values to match food data
caloric_matrix = caloric_values 

# Calculate calorie breakdown for each food
calorie_breakdown = food_data * caloric_matrix
print(calorie_breakdown)
import numpy as np

temperatures = np.array([
    [30, 32, 34, 33, 31],  
    [25, 27, 29, 28, 26], 
    [20, 22, 24, 23, 21]  
])

# Correction factors for each city
corrections = np.array([1.5, -0.5, 2.0])

adjusted_temperatures = temperatures + corrections[:, np.newaxis]
print(adjusted_temperatures)
import numpy as np

# Example image data (3x3 grayscale image)
image = np.array([
    [100, 120, 130],
    [90, 110, 140],
    [80, 100, 120]
])

mean = image.mean(axis=0)   # Mean per column (feature-wise)
std = image.std(axis=0)     # Standard deviation per column

# Normalize using broadcasting
normalized_image = (image - mean) / std
print(normalized_image)
import numpy as np

data = np.array([
    [10, 20],
    [15, 25],
    [20, 30]
])

feature_mean = data.mean(axis=0)

# Center data using broadcasting
centered_data = data - feature_mean
print(centered_data)
import numpy as np

a1 = np.array([2,4,6,8,10 ])
number= 2
result = a1 + number
print(result)
import numpy as np
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
result = a1 + a2
print(result)  
import numpy as np
a1 = np.array([1, 2, 3, 4])
result = a1 * 2
print(result)  
import numpy as np
a1 = np.array([10, 20, 30])
result = a1 > 15
print(result)  
import numpy as np
a1= np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
result = np.dot(a1, a2) 
print(result)
import numpy as np

def custom_func(x):
    return x**2 + 2*x + 1

a1 = np.array([1, 2, 3, 4])
result = custom_func(a1)
print(result) 
import numpy as np
a1 = np.array([1, 2, 3])
result_sum = a1.sum()
result_mean = a1.mean()
print(result_sum)   
print(result_mean)  
import numpy as np
import time

start_time = time.time()
vectorized_sum = np.sum(np.arange(15000))
print("Vectorized sum:", vectorized_sum)
print("Time taken by vectorized sum:", time.time() - start_time)

start_time = time.time()
iterative_sum = sum(range(15000)) 
print("\nIterative sum:", iterative_sum)
print("Time taken by iterative sum:", time.time() - start_time)
