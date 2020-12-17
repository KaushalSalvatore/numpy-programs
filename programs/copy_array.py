from numpy import *

array_0 = array([1,2,3,4,5,6,7,8,9])
array1 = array_0 + 5
print(array1)

# multiple array

array2 = array([1,2,3,4,5,6,7,8,9])
array3 = array([1,2,3,4,5,6,7,8,9])
array4=array2+array3
print(array4)
print(sin(array4)) # cos , ten , mean , sum of element , max , min , unique , sort array ,  concatanation



array5 = array4 # copy array
array5 = array4.view() # view use for diffent address

print(array5)


print(id(array5))
print(id(array4))  # copy array in the same address

# # shallow copy : if we change in one array its automatic replace in 2nd array and for this we use copy
#
array5 = array4.copy() # deep copy
print(array5)
#




