# follow CS231 numpy tutorial
import numpy as np

def quicksort(arr):
    if(len(arr) <= 1):
        return arr
    pivotindex = len(arr) // 2
    pivot = arr[pivotindex]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left, middle, right)
    return quicksort(left) + middle + quicksort(right)

sorted = quicksort([3,6,76,2,4,8,4,8,32,8])
print(sorted)
print("*******quicksort end***********")

a = np.array([1, 2, 3]) # create rank 1 array
print(type(a), a.shape)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

# np array indexing
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# slice first two rows and columns 1 and 2
s = a[:2, 1:3]
print(s)

