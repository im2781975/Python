"""            NumPy            """
import numpy as np
ar = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]); print(ar, ar.shape)
ar = np.array([
    [[10, 25, 70], [30, 45, 55], [20, 45, 7]],  
    [[50, 65, 8], [70, 85, 10], [11, 22, 33]], 
    [[19, 69, 36], [1, 5, 24], [4, 20, 96]]])
x = ar.sum(-1)
print(ar, ar[:, [0, 2]], ar[x % 10 == 0])
ar = np.array(
    [[1, 20, 3, 1], [40, 5, 66, 7], [70, 88, 9, 11], [80, 100, 50, 77], [1, 8.5, 7.9, 4.8]])
print(ar[[0, 1, 2],[0, 0, 1]], ar, ar[[0, 1]])
ar = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]); print(ar, ar.shape, ar.ndim, ar.size, ar + 10)
print(ar.dtype, ar.itemsize, ar[0 : 2], ar[1 : 3], ar[0 : 2, 1 : 3], ar[1, 2], ar.flatten())
ar = np.array([[[1, 0, 1], [0, 1, 0]], [[1, 1, 0], [0, 0, 1]]]); print(np.packbits(ar, axis = -1))
ar = np.array([[2], [7], [23]], dtype = np.uint8); print(np.unpackbits(ar, axis = 1))
ar = np.array([[2], [7], [23]], dtype = np.uint8)
ar = np.array([2, 4, 6, 8], ndmin = 3); print(ar, ar.shape, ar + 10)
ar = np.array([(1, 2), (3, 4), (5, 6), (7, 8)]); print(ar, ar.shape)
ar = np.array([1, 2, 3, 4, 5, 6]); print(ar, ar[1 : 4], ar + 1)
print(ar.reshape(2, 3), ar[ar > 3], ar[(ar > 2) & (ar < 6)])
ar[1 : 3] = 99; ar.sort(); print(ar)
a, b, c = np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([[2, 3, 4], [7, 8, 9]])
print(a + b, a - b, a * b, a / b, a > 2, a * 2, a + c, a * c)
x, y = np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])
print(np.dot(x, y), x + 10, x.flatten(), x.flatten('F'),)
import math as mt
ar = [0, mt.pi / 2, np.pi / 3, np.pi]
print(np.sin(ar), np.cos(ar), np.sinh(ar), np.cosh(ar))
ar = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print(np.around(ar), np.around(ar, decimals = 3), np.round(ar), np.round(ar, decimals = 3))
lst = [1, 2, 3, 4, 5]; print(np.array(lst))
print(np.zeros((3, 4)), np.zeros(5), np.ones((2, 3)), np.ones((2, 3, 4)), np.ones(5))
print(np.empty((3, 4)), np.full((2, 2), 7), np.full((3, 3), 5), np.full((3, 4), 5))
print(np.zeros((2, 3), order = 'C')) #order = 'F'
print(np.ones((2, 3), order = 'F')) #order = 'C'
print(np.ones(4, dtype = int), np.random.randint(1, 10, size = (3, 3)))
print(np.random.rand(2, 3), np.random.rand(4, 4, 4))
ar = np.arange(20); print(ar[15], ar[-8 : 17 : 1], ar[10:])
print(np.arange(0, 10, 2), np.arange(5, 10), np.arange(10), np.arange(0, 1, 0.2))
print([np.array([3, 1, 2 ])])
ar = np.arange(0, 20, 3); print(ar[ar > 10])
print(np.linspace(0, 1, 5), np.linspace(0, 1, num = 10))
print(np.linspace(0, 1, num = 25).reshape(5, 5), np.linspace(0, 1, num = 10, endpoint = False))
array, step = np.linspace(0, 10, num = 5, retstep = True); print(step)
print(np.eye(3), np.eye(3, 4), np.eye(4, k = 1))
print(np.diag([1, 2, 3]), [('f', 'f4'), ('i', 'i4')])

x, y, lst, ist = 10, 11, [2, 8, 125], [3, 3, 115]
print(np.reciprocal(x), np.bitwise_and(x, y), np.bitwise_or(x, y), np.bitwise_xor(x, y))
print(np.invert(x), np.left_shift(lst, ist), np.right_shift(x, y), np.binary_repr(lst[1]), np.binary_repr(lst[2]))
print(np.binary_repr(lst[1], width = 4), np.binary_repr(lst[2], width = 7), np.divide(lst, ist), np.cbrt(lst), np.cbrt(ist))
print(np.clip(lst, a_min = 2, a_max = 6), np.asarray(lst))
ar = [1, 3, 5, 7, 9, 2 ** 8]
print(np.exp(ar), np.log(ar), np.log(2 ** 8), np.log(4 ** 4))
print(np.isreal([1 + 1j, 0j]), np.isreal([1, 0]), np.conj(2 + 4j), np.conj(5 - 8j))
print(np.char.lower(['GEEKS', 'FOR']), np.char.lower('GEEKS'), np.char.split('geeks for geeks'))
print(np.char.split('geeks, for, geeks', sep = ','), np.char.join('-', 'geeks'), np.char.join(['-', ':'], ['geeks', 'for']))
ar = np.array(['geeks', 'for', 'geeks'])
print(np.char.count(ar, 'geek'), np.char.count(ar, 'fo'), np.char.rfind(ar, 'geek'), np.char.rfind(ar, 'fo'), np.chararray((2, 3)))
print(np.char.isnumeric('geeks'), np.char.isnumeric('12geeks'), np.char.equal('geeks','for'), np.char.not_equal('geeks', 'for'), np.char.greater('geeks','for'))
ar[:] = 'Hello'; print(ar)
data = np.array([[0.8, 2.9, 3.9], [52.4, 23.6, 36.5], [55.2, 31.7, 23.9], [14.4, 11, 4.9]])
print(data * np.array([3, 3, 8]))
print(ar) #print(ar[[1, 2, 3]])
tmp = np.array([[30, 32, 34, 33, 31],
    [25, 27, 29, 28, 26], [20, 22, 24, 23, 21]])
corr = np.array([1.5, -0.5, 2.0])
print(tmp + corr[:, np.newaxis], tmp, tmp[1])
img = np.array([ [100, 120, 130], [90, 110, 140], [80, 100, 120] ])
mean = img.mean(axis = 0)
std = img.std(axis = 0)
print((img - mean) / std)
data = np.array([ [10, 20], [15, 25], [20, 30]])
feature = data.mean(axis = 0)
print(data - feature, img, img[[0, 2]])
cube = np.array([ [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]); print(cube[1, 2, 0])
def custom(x):    return x ** 2 + 2 * x + 1
print(custom(np.array([1, 2, 3, 4, 5])))
import numpy as np
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
m = 4
x = ar.size // m
shape = ar.reshape((m, x))
print(shape, str(ar))
print(np.reshape(ar, (2, 8)), ar.reshape((2, 2, 4)))
print(ar.reshape((2, 2, -1)), ar.reshape((4, -1)))
ar = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ar)
print(ar.reshape(9)); print(ar.reshape(1, 9))

x, y = np.array([[1, 2, 3], [4, 5, 6]]), np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate((x.flatten(), y.flatten())))
print(np.zeros_like(x.flatten()), x.flatten().max())
print(np.sort(y, axis=0)) 
# axis = -1 / None

arr = np.array([9, 3, 1, 7, 4, 3, 6])
b = np.argsort(arr); print(arr, b)
c = np.zeros(len(b), dtype = int) 
for i in range(0, len(b)):
    c[i] = arr[b[i]] 
print(c) 
arr = np.array([9, 3, 1, 3, 4, 3, 6]) 
ray = np.array([4, 6, 9, 2, 1, 8, 7]) 
for (i, j) in zip(arr, ray):    print(i, ' ', j)
print(np.lexsort((ray, arr)))
arr.sort(); print(arr)
b = sorted(ray); print(b)
tmp = np.argsort(arr)
c = np.zeros(len(tmp), dtype = int) 
for i in range(0, len(tmp)): 
    c[i]= arr[tmp[i]] 
print(c) 
tmp = np.where(arr == 4); print("{}{}".format(tmp, arr))
idx = np.where(arr == 4)[0]; print(idx)
print("left-most index =", np.searchsorted(arr, 3, side="left"))
print("right-most index =", np.searchsorted(arr, 3, side="right"))
ar = np.arange(12).reshape(3, 4)
print(ar, np.argmax(ar), np.dot(5, 6), np.argmax(ar, axis = 0))
ar = np.arange(9).reshape(1, 3, 3); print(ar)
br = np.squeeze(ar, axis = 0); print(br)
print(ar.shape, br.shape)

