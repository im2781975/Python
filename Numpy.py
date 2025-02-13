
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
#methid
