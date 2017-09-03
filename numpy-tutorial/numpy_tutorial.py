# follow CS231 numpy tutorial

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