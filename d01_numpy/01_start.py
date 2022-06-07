import numpy as np

print(np.__version__)

arr = np.arange(10)
print(arr)
print(arr.shape)
print(arr.dtype)

print(arr[5:8])

arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
arr_slice[:] = 64
print(arr)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names, data, sep='\n')

print(names == "Bob")
print(data[names == "Bob"])

converse = names == "Bob"
print(data[converse])

arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[2:5, 1:3])
print(arr[[1, 3, 5, 7], [0, 3, 1, 2]])

arr = np.arange(15).reshape((3, 5))
print(arr.T)

print(np.dot(arr.T, arr))

x = np.random.randn(8)
y = np.random.randn(8)

print(x, y, np.maximum(x, y), sep='\n')

points = np.arange(-5, 5, 0.01)
print(points)
xs, ys = np.meshgrid(points, points)
print(xs)
z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

np.save('z.npy', z)

xarr = np.arange(1.1, 1.6, 0.1)
yarr = np.arange(2.1, 2.6, 0.1)
print(xarr, yarr, sep='\n')
cond = np.array([True, False, True, True, False])

print(np.where(cond, xarr, yarr))

arr = np.random.randn(5, 4)
print(arr.mean())
