
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]); print(arr, arr.shape)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr, "\n", arr.shape, arr.ndim, arr.size, arr.dtype, arr.itemsize, arr[0 : 2], arr[1 : 3])
print(arr + 10, arr.shape)
print(arr[0 : 2, 1 : 3], arr[1, 2])
arr = np.array([2, 4, 6, 8, 10], ndmin = 6)
print(arr, arr.shape)
arr = np.array([(1, 2), (3, 4), (5, 6), (7, 8)])
print(arr, arr.shape)
arr = np.array([1, 2, 3, 4, 5])
print(arr[2], arr[1 : 4], arr + 1)
arr[1 : 3] = 99; print(arr)
arr.sort(); print(arr)
a, b, c = np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([[1, 2, 3], [4, 5, 6]])
print(a + b, a - b, a * b, a / b, a * 2, a > 2)
print(a + c, a * c)
mat, rix = np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])
print(np.dot(mat, rix))
print(mat + 10, mat.flatten(), mat.flatten('F'), )
arr = np.array([1, 2, 3, 4, 5, 6]); print(arr.reshape(2, 3), arr[arr > 3], arr[0], arr[1 : 4], arr[(arr > 2) & (arr < 6)])  
arr = np.array([[1, 2, 3], [4, 5, 6]]); print(arr[1, 2], arr.flatten())
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr[[0, 1, 2],[0, 0, 1]])
arr = np.array(
    [[1, 20, 3, 1], [40, 5, 66, 7], [70, 88, 9, 11], 
    [80, 100, 50, 77], [1, 8.5, 7.9, 4.8]])
print(arr, arr[[0, 1]])
arr = np.array(
    [[[10, 25, 70], [30, 45, 55], [20, 45, 7]],  
    [[50, 65, 8], [70, 85, 10], [11, 22, 33]]])
print(arr, arr[:, [1]])
arr = np.array([
    [[10, 25, 70], [30, 45, 55], [20, 45, 7]],  
    [[50, 65, 8], [70, 85, 10], [11, 22, 33]], 
    [[19, 69, 36], [1, 5, 24], [4, 20, 96]]]) 
print(arr, arr[:, [0, 2]])

row = arr.sum(-1)
print(arr[row % 10 == 0])
lst = [1, 2, 3, 4, 5]; print(np.array(lst))
print(np.zeros((3, 4)))
print(np.zeros(5))
print(np.zeros((2, 3), order = 'C'))
print(np.zeros((2, 3), order = 'F'))
print(np.ones(5))
print(np.ones((2, 3)))
print(np.ones((2, 3), order = 'C'))
print(np.ones((2, 3), order = 'F'))
print(np.ones(4, dtype = int))
print(np.ones((2, 3, 4)))
print(np.empty((3, 4)))
print(np.empty((3, 4)))
print(np.full((2, 2), 7))
print(np.full((3, 3), 5))
print(np.full((3, 4), 5))
print(np.random.rand(2, 3))
print(np.random.rand(4, 4, 4))
print(np.random.randint(1, 10, size = (3, 3)))
arr = np.arange(20)
print(arr[15], arr[-8 : 17 : 1], arr[10:])
print(np.arange(0, 10, 2))
print(np.arange(5, 10))
print(np.arange(10))
print(np.arange(0, 1, 0.2))
arr = np.arange(10, 1, -2); print(arr)
print([np.array([3, 1, 2 ])])
seq = np.arange(0, 20, 3); print(seq[seq > 10])
print(np.linspace(0, 1, 5))
print(np.linspace(0, 1, num = 10))
print(np.linspace(0, 1, num = 25).reshape(5, 5))
print(np.linspace(0, 1, num = 10, endpoint = False))
array, step = np.linspace(0, 10, num = 5, retstep = True); print(step)
"""
print(np.eye(3))
print(np.eye((3, 4)))
print(np.eye(4, k = 1)) """
print(np.diag([1, 2, 3]))
print([('f', 'f4'), ('i', 'i4')])

#Operation
import numpy as np
x, y = 10, 11
lst, ist = [2, 8, 125], [3, 3, 115]
print(np.reciprocal(x))
print(np.bitwise_and(x, y))
print(np.bitwise_or(x, y))
print(np.bitwise_xor(x, y))
print(np.invert(x))
print(np.left_shift(x, y))
print(np.right_shift(x, y))
print(np.binary_repr(x))
print(np.bitwise_and(lst, ist))
print(np.bitwise_or(lst, ist))
print(np.bitwise_xor(lst, ist))
print(np.invert(lst))
print(np.left_shift(lst, ist))
print(np.right_shift(lst, ist))
print(np.binary_repr(lst[1]))
print(np.binary_repr(lst[1], width = 4))
print(np.binary_repr(lst[2]))
print(np.binary_repr(lst[2], width = 7))
print(np.clip(lst, a_min = 2, a_max = 6))
print(np.divide(lst, ist))
print(np.cbrt(lst), np.cbrt(ist))
print(np.asarray(lst))
import numpy as np
arr = np.array([[[1, 0, 1], [0, 1, 0]], [[1, 1, 0], [0, 0, 1]]])
print(np.packbits(arr, axis = -1))
arr = np.array([[2], [7], [23]], dtype = np.uint8)
print(np.unpackbits(arr, axis = 1))
import math
arr = [0, math.pi / 2, np.pi / 3, np.pi]
print(np.sin(arr), np.cos(arr), np.sinh(arr), np.cosh(arr))
arr = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print(np.around(arr))
print(np.around(arr, decimals = 3))
print(np.round(arr))
print(np.round(arr, decimals = 3))
arr = [1, 3, 5, 7, 9, 2 ** 8]
print(np.exp(arr), np.log(arr))
print(np.log(4 ** 4), np.log(2 ** 8))
print(np.isreal([1 + 1j, 0j]))
print(np.isreal([1, 0]))
print(np.conj(2 + 4j), np, conj(5 - 8j))
print(np.char.lower(['GEEKS', 'FOR']))
print(np.char.lower('GEEKS'))
print(np.char.split('geeks for geeks'))
print(np.char.split('geeks, for, geeks', sep = ','))
print(np.char.join('-', 'geeks'))
print(np.char.join(['-', ':'], ['geeks', 'for']))
arr = np.array(['geeks', 'for', 'geeks'])
print(np.char.count(arr, 'geek'))
print(np.char.count(arr, 'fo'))
print(np.char.rfind(arr, 'geek'))
print(np.char.rfind(art, 'fo'))
print(np.char.isnumeric('geeks'))
print(np.char.isnumeric('12geeks'))
print(np.char.equal('geeks','for'))
print(np.char.not_equal('geeks', 'for'))
print(np.char.greater('geeks','for'))
arr = np.chararray((2, 3))  
arr[:] = 'Hello'; print(arr)
data = np.array([[0.8, 2.9, 3.9], [52.4, 23.6, 36.5],
    [55.2, 31.7, 23.9], [14.4, 11, 4.9]])
print(data * np.array([3, 3, 8]))
print(arr, arr[[1, 2, 3]])
temp = np.array([
    [30, 32, 34, 33, 31], [25, 27, 29, 28, 26], 
    [20, 22, 24, 23, 21] ])
correct = np.array([1.5, -0.5, 2.0])
print(temp + correct[:, newaxis])
print(temp, temp[1])
image = np.array([
    [100, 120, 130], [90, 110, 140],
    [80, 100, 120] ])
mean = image.mean(axis = 0) 
std = image.std(axis = 0)     
print((image - mean) / std)
data = np.array([
    [10, 20], [15, 25], [20, 30] ])
feature = data.mean(axis = 0)
print(data - feature)
print(image, image[[0, 2]])
cube = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(cube[1, 2, 0])
def custom(x):
    return x**2 + 2*x + 1
print(custom(np.array([1, 2, 3, 4])))
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
n = arr.size(); N = 4
M = n // N
reshape = arr.reshape((N, M))
print(reshape, str(arr))
print(np.reshape(arr, (2, 8)))
print(arr.reshape((2, 2, 4)))
print(arr.reshape((2, 2, -1)))
print(arr.reshape((4, -1)))
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr, arr.reshape((9)), arr.reshape((1, 5)))

arr = np.array([[1, 2, 3], [4, 5, 6]])
ray = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate((arr.flatten(), ray.flatten())))
print(np.zeros_like(arr.flatten()))
print(arr.flatten().max())
print(np.sort(ray, axis = 0))
print(np.sort(ray, axis = -1)) 
print(np.sort(ray, axis = None))
arr = np.array([9, 3, 1, 7, 4, 3, 6])
b = np.argsort(arr); print(arr, b)
c = np.zeros(len(b), dtype = int) 
for i in range(0, len(b)): 
    c[i]= a[b[i]] 
print(c) 

arr = np.array([9, 3, 1, 3, 4, 3, 6]) 
ray = np.array([4, 6, 9, 2, 1, 8, 7]) 
for (i, j) in zip(arr, ray): 
    print(i, ' ', j) 
print(np.lexsort((ray, arr)))
arr.sort(); print(arr)
b = sorted(ray); print(b)
tmp = np.argsort(arr)
c = np.zeros(len(tmp), dtype = int) 
for i in range(0, len(tmp)): 
    c[i]= a[tmp[i]] 
print(c) 

arr = np.array([10, 32, 30, 50, 20, 82, 91, 45]) 
print("arr = {}".format(arr)) 
tmp = np.where(arr == 30) 
print("i = {}".format(tmp))
import numpy as np

arr = np.array([10, 32, 30, 50, 20, 82, 91, 45]); print("arr =", arr)
idx = np.where(arr == 30)[0]; print(idx)
arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6] 
print("left-most index =", np.searchsorted(arr, 3, side="left"))
print("right-most index =", np.searchsorted(arr, 3, side="right"))

import numpy as np
import array
arr = np.arange(12).reshape(3, 4)
print(arr,np.argmax(arr), np.argmax(arr,  axis = 0), np.argmax(array, axis = 1))
print(np.dot(5, 4))

arr = np.arange(9).reshape(1, 3, 3)  
print (arr)   
out = inp.squeeze(arr, axis = 0)  
print (out)   
print(arr.shape, out.shape)
out = np.squeeze(in_arr, axis = 1)  
  
print (out)   
print(arr.shape, out.shape) 

arr = [np.nan, 4, 2, 3, 1]
ray = np.array([[np.nan, 4], [1, 3]])
print(np.nanargmax(arr))
print(np.nanargmax(ray))
print(np.nanargmax(ray, axis = 1))
print(np.arange(8))
print(np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]]))
print(np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis = 0))
arr = np.array([1, 2]); ray = np.array([3, 4]) 
print(np.concatenate((arr, ray)))
print(np.hstack((arr, ray)))
arr = np.array([[1, 2]]); ray = np.array([[3, 4]]) 
print(np.vstack((arr, ray))) 
arr = np.array([[1, 2, 3], [-1, -2, -3]]) 
ray = np.array([[4, 5, 6], [-4, -5, -6]]) 
print(np.hstack((arr, ray)))
print(np.vstack((arr, ray)))
arr = np.array([[1, 2], [3, 4]]) 
ray = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr, ray), axis = 1))
arr = np.array([
    [10.5, 22.5, 3.8], [41, np.nan, np.nan]])
print(arr)
print(arr[~np.isnan(arr).any(axis = 1)])
arr = np.array([[10.5, 22.5, 3.8], 
    [23.45, 50, 78.7], [41, np.nan, np.nan]])
print(arr)
print(arr[~np.isnan(arr).any(axis = 1)])
arr = np.array([[10.5, 22.5, 3.8, 5],
    [23.45, 50, 78.7, 3.5], [41, np.nan, np.nan, 0],
    [20, 50.20, np.nan, 2.5], [18.8, 50.60, 8.8, 58.6]])
print(arr, n_arr[~np.isnan(arr).any(axis=1)])
arr = np.array([1, 2, 3, 4]) 
ray = np.array([5, 6, 7, 8]) 
print(np.stack((arr, ray), axis = 1))

a = np.array([[1, 1], [1, 1]]) 
b = np.array([[2, 2, 2], [2, 2, 2]]) 
c = np.array([[3, 3], [3, 3], [3, 3]]) 
d = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]]) 
print(np.block([[a, b], [c, d] ]))
arr = np.arrange(13)
print(np.array_split(arr, 4))
print(np.split(arr, 2))
x = np.arange(5)
y = np.arange(10).reshape(2,5) 
print(x, y)
for a, b in np.nditer([x, y]): 
    print("%d:%d" % (a, b),)
arr = np.arange(3) 
print(arr, np.mean(arr, axis = 1, out = arr)) 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.array_split(arr, 3))
arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
print(np.split(arr, 3, axis = 1))

matrix = np.array([
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(matrix, np.vsplit(matrix, 2))
arr = np.array([[1, 2, 3, 4],
    [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr, np.hsplit(arr, 2))

arr = np.arange(24).reshape((2, 3, 4))
print(np.dsplit(arr, 2))
import numpy as np 
arr = [20, 2, .2, 10, 4] 
ray = [[14, 17, 12, 33, 44], [15, 6, 27, 8, 19], 
    [23, 2, 54, 1, 4,]] 
print(np.mean(arr))
print(np.sum(arr)) 
print(np.sum(ray))
print(np.sum(arr, dtype = np.uint8)) 
print(np.sum(ray, dtype = np.uint8)) 
print(np.sum(arr, dtype = np.float32))
print(np.sum(ray, dtype = np.float32))
print (np.sum(arr).dtype == np.uint) 
print (np.sum(ray).dtype == np.uint) 
print (np.sum(arr).dtype == np.float) 
print (np.sum(ray).dtype == np.float) 
print(np.sum(ray, axis = 0))
print(np.sum(ray, axis = 1))
print(np.sum(ray, axis = 1, keepdims = True))
print(np.mean(ray))  
print(np.mean(ray, axis = 0))  
print(np.mean(ray, axis = 1)) 
x = np.array([[1, 2], [4, 5]]) 
y = np.array([[7, 8], [9, 10]]) 
print(np.add(x, y), x.T) 
print(np.subtract(x, y))
print(np.divide(x, y))
print (np.multiply(x,y)) 
print (np.dot(x,y)) 
print (np.sqrt(x)) 
print (np.sum(y)) 
print (np.sum(y, axis = 0))
print (np.sum(y, axis = 1)) 
x = np.array([1, 2, 3])
print(x.sum(), x.mean())
A, B = [[1, 2], [4, 5]], [[7, 8], [9, 10]]
rows = len(A) 
cols = len(A[0]) 
C = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        C[i][j] = A[i][j] + B[i][j] 
D = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        D[i][j] = A[i][j] - B[i][j] 
E = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
    for j in range(cols): 
        E[i][j] = A[i][j] / B[i][j] 
print(C, D, E)
matrix = np.matrix([[1, 2, 3], [4, 5, 6]])
print(matrix, matrix.transpose())
print(np.linalg.inv(matrix))
print(np.linalg.matrix_rank(matrix))
print( np.trace(matrix))
print(np.linalg.det(matrix))
print( np.linalg.inv(matrix))
 
print(np.linalg.matrix_power(matrix, 3))
rix = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]') 
print(rix, rix.transpose())
mat = np.matrix([[1, 2], [3, 4]])
rix = np.matrix([[5, 6], [7, 8]])
print(mat * rix.transpose())
arr = np.array(
    [[6, 1, 1, 3], [4, -2, 5, 1],
     [2, 8, 7, 6], [3, 1, 9, 7]])
print(np.linalg.inv(arr))
arr = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])
print(np.linalg.inv(arr))
x = np.eye(3) 
y = np.ones((3, 3)) * 3
print(x.dot(y), x.dot(y).dot(y))
x = np.matrix('[4, 1; 12, 3]') 
print(x.var())
y = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]') 
print(y.var())
import numpy as np
from numpy import linalg
a = np.array([[1, -2j], [2j, 5]])
c, d = linalg.eigh(a)
print(a, c, d)
a = np.diag((1, 2, 3))
c, d = linalg.eig(a)
print(a, c, d)

vec = 2 + 3j
tor = 4 + 5j
print(np.vdot(vec, tor))
a = np.array([[1, 2], [3, 4]])
b = np.array([8, 18])
print((np.linalg.solve(a, b)))
arr = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(np.linalg.det(arr))
print(np.trace(arr))

import numpy as np 
arr = np.array([[10, 22], [13, 6]])
q, r =  np.linalg.qr(arr) 
print(q, r)
arr = np.array([[0, 1], [1, 0], [1, 1], [2, 2]]) 
q, r =  np.linalg.qr(arr) 
print(q, r)
arr = np.array([[5, 11, -15],
    [12, 34, -51], [-24, -43, 92]], dtype = np.int32) 
q, r = np.linalg.qr(arr); print(q, r)
from numpy import linalg 
print(linalg.eigvals([[1, 2], [3, 4]]))
print(np.random.randint(low = 0, high = 3, size = 5))
print(np.random.randint(low = 4, size = (2, 3)))
print(np.random.randint(2, 10, (2, 3, 4)))
print(np.random.rand(5))
print(np.random.rand(3, 4))
print(np.random.rand(2, 2 ,2))
print(np.random.normal(size = 5))
print(np.random.normal(0.0, 1.0, 5))

arr = np.array([2, 4, 6])
ray = np.array([[1, 3, 5], [7, 9, 11]])
print(arr + ray)

import time
start_time = time.time()
print(np.sum(np.arange(15000)))
print(time.time() - start_time)
start_time = time.time()
iterative_sum = sum(range(15000)) 
print("\nIterative sum:", iterative_sum)
print("Time taken by iterative sum:", time.time() - start_time)

angles = np.array([0, 30, 45, 60, 90, 180])  
radians = np.deg2rad(angles)
sine_value = np.sin(radians) 
print(np.sin(radians)) 
print(np.rad2deg(np.arcsin(sine_value))) 
sineh_value = np.sinh(radians) 
print(np.sinh(radians))
print('Inverse Sine hyperbolic:') 
print(np.sin(sineh_value))  

base = 4
height = 3
print(np.hypot(base, height)) 
weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45]) 
print(np.amin(weight), np.amax(weight)) 
print(np.ptp(weight))
print(np.percentile(weight, 70))
print(np.mean(weight)) 
print(np.median(weight))
print(np.std(weight))
print(np.var(weight))
print(np.average(weight)) 

even = np.array([0, 2, 4, 6, 8, 16, 32]) 
odd = np.array([1, 3, 5, 7, 9, 17, 33]) 
print(np.bitwise_and(even, odd))
print(np.bitwise_or(even, odd)) 
print(np.bitwise_xor(even, odd))
print(np.invert(even))
print(np.left_shift(even, 1))
print(np.right_shift(even, 1)) 
print([1, 2, 3, 4, 5] in arr.tolist()) 
print([16, 17, 20, 19, 18] in arr.tolist()) 
print([3, 2, 5, -4, 5] in arr.tolist()) 
print([11, 12, 13, 14, 15] in arr.tolist()) 
arr = np.array([[[2, 2, 2], [2, 2, 2]]]np
print(arr.shape)   
x = np.squeeze(arr))
print(x, x.shape)  

import numpy as np
import calc  
import sys
print(sys.path)
a = np.array([0, 3, 4, 3, 5, 4, 7])
print("Occurrences of 3:", np.sum(a == 3)) 
print("10 + 2 =", calc.add(10, 2))
List = [1, 4, True, 800, "python", 27, "hello"]
print(random.choice(List)) 
