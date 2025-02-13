
import numpy as np

#1D array
arr1 = np.array([1, 2, 3, 4, 5])

#2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

#3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr1)
print(arr2)
print(arr3)
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)  
print("Dimensions:", arr.ndim)  
print("Size:", arr.size) 
print("Data type:", arr.dtype)  
print("Item size:", arr.itemsize)  
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[2]) 
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 6 (element at row 1, column 2)
print(arr_2d[1, 2])  

# Sub-matrix from rows 0-1, columns 1-2
print(arr_2d[0:2, 1:3])  
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 6 (element at row 1, column 2)
print(arr_2d[1, 2])  

# Sub-matrix from rows 0-1, columns 1-2
print(arr_2d[0:2, 1:3])  
import numpy as np 
arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr + arr2)  
print(arr * arr2)  
print(arr - arr2)  
print(arr / arr2) 
import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(np.dot(matrix1, matrix2))  
import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(np.dot(matrix1, matrix2))  
import numpy as np
arr = np.array([[1, 2], [3, 4]])

# Adding 10 to each element of the array
print(arr + 10)  
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)  # 2 rows, 3 columns
print(reshaped_arr)
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened_arr = arr.flatten()
print(flattened_arr)  
# importing numpy module
import numpy as np

# creating list
list = [1, 2, 3, 4]

# creating numpy array
sample_array = np.array(list)

print("List in python : ", list)

print("Numpy Array in python :",
      sample_array)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
import numpy as np

# One-dimensional array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Two-dimensional array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
import numpy as np

# 3x4 array filled with zeros
arr_zero = np.zeros((3, 4))  
print(arr_zero)
import numpy as np 

# 2x3 array filled with ones
arr_one = np.ones((2, 3))  
print(arr_one)
import numpy as np 

# 2x2 array filled with 7
arr_full = np.full((2, 2), 7)
print(arr_full)
import numpy as np 

 # 2x3 array of random floats
arr_rand = np.random.rand(2, 3) 
print(arr_rand)
import numpy as np 

 # 3x3 array of random integers from 1 to 9
arr_int = np.random.randint(1, 10, size=(3, 3)) 
print(arr_int)
import numpy as np 

# Array from 0 to 10 with step 2
arr_range = np.arange(0, 10, 2)  
print(arr_range)
import numpy as np 

# 5 values from 0 to 1
arr_linspace = np.linspace(0, 1, 5)  
print(arr_linspace)
import numpy as np 

# 3x3 identity matrix
identity_matrix = np.eye(3)  
print(identity_matrix)
import numpy as np

# Diagonal matrix with [1, 2, 3] on the diagonal
diag_matrix = np.diag([1, 2, 3])  
print(diag_matrix)
#method. 
import numpy as np 

#create an array 
arr= np.arange(5 , 10)
print(arr)
import numpy as np

# Creating a sequence of numbers from 0 to 9
sequence = np.arange(10)
print("Basic Sequence:", sequence)
import numpy as np 

# Creating a sequence of floating-point numbers from 0 to 1 
# with a step size of 0.2 using np.arange()
sequence = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence)
import numpy as np 

# Creating a sequence of numbers from 0 to 20 
sequence = np.arange(0, 20, 3)

# Filtering the sequence to include only values greater than 10
filtered = sequence[sequence > 10]
print("Filtered Sequence:", filtered)
import numpy as np

#Create 1D array
arr = np.zeros(5)
print(arr)
import numpy as np

# Creating a 2D array with 3 rows and 4 columns
arr = np.zeros((3, 4))

print(arr)
import numpy as np 

# Create an array of tuples with zeros
d = np.zeros((2, 2), dtype=[('f', 'f4'), ('i', 'i4')])
print(d)
import numpy as np 
# Create a 2x3 array in C-order
e = np.zeros((2, 3), order='C')
print("C-order array:", e)

# Create a 2x3 array in F-order
f = np.zeros((2, 3), order='F')
print("F-order array:", f)
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
import numpy as np

# Generate 10 numbers between 0 and 1
array = np.linspace(0, 1, num=10)
print(array)
import numpy as np

# Generate 10 numbers between 0 and 1
array_without_endpoint = np.linspace(0, 1, num=10, endpoint=False)

print(array_without_endpoint)
import numpy as np

# Generate 5 numbers between 0 and 10 and return the step size
array, step = np.linspace(0, 10, num=5, retstep=True)

print("Step Size:", step)
import numpy as np

# Create a 2D array of 5x5 numbers between 0 and 1
array_2d = np.linspace(0, 1, num=25).reshape(5, 5)

print(array_2d)
import numpy as np

# Creating a 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)
import numpy as np

# Creating a 3x5 rectangular matrix
rectangular_matrix = np.eye(3, 5)
print(rectangular_matrix)
import numpy as np

# Creating a 4x4 matrix with diagonal offset
matrix = np.eye(4, k=1)
print(matrix)
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

#Operation
# Python program explaining
# bitwise_and() function

import numpy as geek
in_num1 = 10
in_num2 = 11

print ("Input  number1 : ", in_num1)
print ("Input  number2 : ", in_num2) 
  
out_num = geek.bitwise_and(in_num1, in_num2) 
print ("bitwise_and of 10 and 11 : ", out_num) 
# Python program explaining
# bitwise_and() function

import numpy as geek

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
 
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
  
out_arr = geek.bitwise_and(in_arr1, in_arr2) 
print ("Output array after bitwise_and: ", out_arr) 
# Python program explaining
# bitwise_or() function

import numpy as geek
in_num1 = 10
in_num2 = 11

print ("Input  number1 : ", in_num1)
print ("Input  number2 : ", in_num2) 
  
out_num = geek.bitwise_or(in_num1, in_num2) 
print ("bitwise_or of 10 and 11 : ", out_num) 
# Python program explaining
# bitwise_or() function

import numpy as geek

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
 
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
  
out_arr = geek.bitwise_or(in_arr1, in_arr2) 
print ("Output array after bitwise_or: ", out_arr) 
# Python program explaining
# bitwise_xor() function

import numpy as geek
in_num1 = 10
in_num2 = 11

print ("Input  number1 : ", in_num1)
print ("Input  number2 : ", in_num2) 
  
out_num = geek.bitwise_xor(in_num1, in_num2) 
print ("bitwise_xor of 10 and 11 : ", out_num) 
# Python program explaining
# bitwise_xor() function

import numpy as geek

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
 
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
  
out_arr = geek.bitwise_xor(in_arr1, in_arr2) 
print ("Output array after bitwise_xor: ", out_arr) 
# Python program explaining
# invert() function

import numpy as geek
in_num = 10
print ("Input  number : ", in_num)
  
out_num = geek.invert(in_num) 
print ("inversion of 10 : ", out_num) 
# Python program explaining
# invert() function

import numpy as geek

in_arr = [2, 0, 25]
print ("Input array : ", in_arr)
  
out_arr = geek.invert(in_arr) 
print ("Output array after inversion: ", out_arr) 
# Python program explaining
# left_shift() function

import numpy as geek
in_num = 5
bit_shift = 2

print ("Input  number : ", in_num)
print ("Number of bit shift : ", bit_shift ) 
  
out_num = geek.left_shift(in_num, bit_shift) 
print ("After left shifting 2 bit  : ", out_num) 
# Python program explaining
# left_shift() function

import numpy as geek

in_arr = [2, 8, 15]
bit_shift =[3, 4, 5]
 
print ("Input array : ", in_arr) 
print ("Number of bit shift : ", bit_shift)
  
out_arr = geek.left_shift(in_arr, bit_shift) 
print ("Output array after left shifting: ", out_arr) 
# Python program explaining
# right_shift() function

import numpy as geek
in_num = 20
bit_shift = 2

print ("Input  number : ", in_num)
print ("Number of bit shift : ", bit_shift ) 
  
out_num = geek.right_shift(in_num, bit_shift) 
print ("After right shifting 2 bit  : ", out_num) 
# Python program explaining
# right_shift() function

import numpy as geek

in_arr = [24, 48, 16]
bit_shift =[3, 4, 2]
 
print ("Input array : ", in_arr) 
print ("Number of bit shift : ", bit_shift)
  
out_arr = geek.right_shift(in_arr, bit_shift) 
print ("Output array after right shifting: ", out_arr) 
# Python program explaining
# binary_repr() function

import numpy as geek
in_num = 10

print ("Input  number : ", in_num)

out_num = geek.binary_repr(in_num) 
print ("binary representation of 10 : ", out_num) 
# Python program explaining
# binary_repr() function
import numpy as geek

in_arr = [5, -8 ]
 
print ("Input array : ", in_arr) 

# binary representation of first array  
# element without using width parameter
out_num = geek.binary_repr(in_arr[0])
print("Binary representation of 5")
print ("Without using width parameter : ", out_num) 

# binary representation of first array
# element using width parameter
out_num = geek.binary_repr(in_arr[0], width = 5)
print ("Using width parameter: ", out_num) 

print("\nBinary representation of -8")

# binary representation of 2nd array
# element without using width parameter
out_num = geek.binary_repr(in_arr[1])
print ("Without using width parameter : ", out_num) 

# binary representation of 2nd array
# element  using width parameter
out_num = geek.binary_repr(in_arr[1], width = 5)
print ("Using width parameter : ", out_num) 
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
