
from numpy import *

arr = array([1,2,3,4,5], float)

print(arr)
print(arr.dtype)

arr1 = linspace(0,15) #default in 50 parts
print(arr1)

arr2 = arange(1,15,2)
print(arr2)

arr3 = logspace(1,40,5)
print('%.2f' %arr3[4])

arr4 = zeros(5)
print(arr4)

arr5 = ones(5, int)
print(arr5)