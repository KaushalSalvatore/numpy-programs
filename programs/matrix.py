from numpy import *
array = array([
    [1,2,3],
    [2,3,4],
    [5,6,7]

              ])

print(array)
print(array.dtype)
print(array.view())
print(array.ndim)
print(array.shape)
print(array.size)
arr2 = array.flatten()# convert array to 1d
print(arr2)

arr3 = arr2.reshape(3,3) # 3 row 3 colmn
print(arr3)

m = matrix('1 2 3 ; 6 7 8')

print(m)

print(diagonal(m))

m1 = matrix('1 2 3 ; 6 7 8')

m2 = matrix('1 2 3 ; 6 7 8')

m3 = m1 + m2

m4 = m1 * m2

print(m4)