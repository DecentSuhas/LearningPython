import numpy as np

arr = np.array([[1, 2, 3], [3, 6, 5], [7, 8, 6]])
print(arr)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(b[0])
print(b[0] + b[1])
print('2nd element on 1st row', c[0, 1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 1, 2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[1:])
print(arr[:5])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr1 = np.array([1, 2, 3])
print(arr1.ndim)
arr2 = np.array([4, 5, 6])
print(arr2.ndim)
arr = np.concatenate((arr1, arr2))
print(arr)
print(arr.ndim)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print(arr.ndim)

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
print(arr)

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
newarr = np.subtract(arr1, arr2)
print(newarr)
newarr = np.multiply(arr1, arr2)
print(newarr)
newarr = np.divide(arr1, arr2)
print(newarr)
newarr = np.power(arr1, arr2)
print(newarr)

arr = np.around(3.1666, 1)
print(arr)
arr = np.floor([-3.1666, 3.6667])
print(arr)
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)

arr = np.arange(1, 10)
print(np.log2(arr))
print(np.log10(arr))

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)


num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

x = np.sin(100/2)
print(x)
x = np.cos(100/2)
print(x)
x = np.tan(100/2)
print(x)