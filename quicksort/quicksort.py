"""
Algorithm:
-----------
1. Choose a random element as pivot
2. Partition the items is array w.r.t. pivot, so that all elements in left are smaller than pivot and elements to right
    is greater than pivot.
3. Recursively loop the two halves and do the same operation.

Note: Partitioning puts the pivot in the correct index where it should be in the final array.

QuickSort(array A, l, r)
    if l < r
        partition A around pivot
        recursively sort the first part
        recursively sort the second part

Partition(A, l, r)
    P = A[r]
    i = l - 1
    for j = l to r
        if A[j] > P
            do nothing
        if A[j] < P
            swap A[j] and A[i]
            i++
    swap A[r] and A[i+1]
    return i+1

Time complexity: O(nlog(n))
Space complexity: O(log(n))
"""


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    temp1 = array[high]
    array[high] = array[i+1]
    array[i+1] = temp1
    return i+1


def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p-1)
        quicksort(array, p+1, high)


arrayToSort = [5,7,2,3,9,0,1,8,4,6]
quicksort(arrayToSort, 0, len(arrayToSort)-1)
print(arrayToSort)