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
print(np.ones((2, 3)))
print(np.full((2, 2), 7))
print(np.random.rand(2, 3))
print(np.random.randint(1, 10, size = (3, 3)))
print(np.arange(0, 10, 2))
print(np.arange(5, 10))
print(np.arange(10))
print(np.arange(0, 1, 0.2))
seq = np.arange(0, 20, 3); print(seq[seq > 10])
print(np.linspace(0, 1, 5))
print(np.eye(3))
print(np.diag([1, 2, 3]))
print([('f', 'f4'), ('i', 'i4')])

