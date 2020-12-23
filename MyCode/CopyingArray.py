from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,4])
# arr3 = arr1 + arr2
#
# print(arr3)
#
# print(sin(arr3))
# print(log(arr3))
# print(sqrt(arr3))
# print(min(arr3))
# print(max(arr3))
#
# print(concatenate([arr1,arr2]))

arr3 = arr1
print(arr3)
print(id(arr1))
print(id(arr3))

arr4 = arr1.view()
print(id(arr1))
print(id(arr4))

arr5 = arr1.copy()
print(arr5)
print(id(arr5))