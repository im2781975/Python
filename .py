import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]); print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr, "\n", arr.shape, arr.ndim, arr.size, arr.dtype, arr.itemsize)
print(arr[0 : 2, 1 : 3], arr[1, 2])
arr = np.array([1, 2, 3, 4, 5])
print(arr[2], arr[1 : 4])

a, b = np.array([1, 2, 3]), np.array([4, 5, 6])
print(a + b, a - b, a * b, a / b)
mat, rix = np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])
print(np.dot(mat, rix))
print(mat + 10)
arr = np.array([1, 2, 3, 4, 5, 6]); print(arr.reshape(2, 3))
arr = np.array([[1, 2, 3], [4, 5, 6]]); print(arr.flatten())
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
print(np.random.randint(1, 10, size = (3, 3)))
print(np.arange(0, 10, 2))
print(np.arange(5, 10))
print(np.arange(10))
print(np.arange(0, 1, 0.2))
seq = np.arange(0, 20, 3); print(seq[seq > 10])
print(np.linspace(0, 1, 5))
print(np.linspace(0, 1, num = 10))
print(np.linspace(0, 1, num = 25).reshape(5, 5))
print(np.linspace(0, 1, num = 10, endpoint = False))
array, step = np.linspace(0, 10, num = 5, retstep = True); print(step)
print(np.eye(3))
print(np.eye((3, 4)))
print(np.eye(4, k = 1))
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
