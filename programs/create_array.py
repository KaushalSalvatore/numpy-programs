from numpy import *

#creating array methods

#1. using array

array = array([1,2,3,4,5,6,7,8,9.0],int)

#array1 = array([1,2,3,4,5,6,7,8,9.0],float)

print(array.dtype) #dtype check array type


#print(array1) #dtype check array type

#2. using linespace

arr = linspace(1,12)

print(arr)

#3. using arange()

arr1 = arange(1,23,3)

print(arr1)

# using logspace

arr2 = logspace(1,20,5)

print(arr2)

#using zeors() and once()

arr3 = ones(5) #arr3 = ones(5, int) for integer value

arr4 = zeros(5)

print(arr4)

