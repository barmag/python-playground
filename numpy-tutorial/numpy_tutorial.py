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

#arange
a = np.arange(10.4) #stop at 10.4 and start at 0 with step 1 and data type float
print(f"arange(10.4) is {a}")

a = np.arange(0.5, 10, 0.8)
print(f"arange(0.5, 10, 0.8) is {a}")
print(f"arange result type: {type(a)}")
print(f"arange shape: {a.shape}")

#linspace
a = np.linspace(1, 10) #return 50 elements between 1, and 10
print(f"np.linspace(1, 10) is {a}")

a = np.linspace(1, 10, num=10, endpoint=False) #returns 10 elements between 1, 10 excluding 10
print(f"linspace(1, 10, num=10, endpoint=False) is : {a}")

a, spacing = np.linspace(1, 10, num=10, endpoint=False, retstep=True)
print(f"spacing is: {spacing}")

# reshape
a = np.arange(28).reshape(7, 4)
print(f"reshaped one dim array {a}")
a = a.reshape(-1)
print(f"reshpaed back {a}")

# slicing with step
b = a[::2]
print(f"slicing with step {b}")
