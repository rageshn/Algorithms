"""
Also known as Quick Select algorithm.

Goal: In an array with n distinct elements, return the k'th order statistics i.e., k'th smallest element in an array.

Algorithm:
-----------
RandomizedSelection(array A, left, right, statistics i)
    if left = right
        return A[1eft]
    Choose pivot P from A uniformly at random
    Partition A around P
        Let j = new index of P
    if j == i
        return A[P]
    else if i < j
      right := j-1
      return RandomizedSelection(1st part of A, left, right, i)
   else
      left := j+1
      return RandomizedSelection(2nd part of A, left, right, i - P + left - 1)

partition(array A, left, right)
    pivot = arr[right]
    i = left - 1
    for j = left to right
        if A[j] < pivot
            swap(A[i], A[j])
            i++
    swap(A[i+1], A[r])
    return i+1


Time Complexity: O(n)
Worst case: O(n^2)
"""


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i = i + 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp1 = array[right]
    array[right] = array[i+1]
    array[i+1] = temp1
    return i + 1


def randomizedselection(A, left, right, k):
    if left == right:
        return A[left]

    index = partition(A, left, right)
    if k == index:
        return A[index]
    elif k < index:
        right = index - 1
        return randomizedselection(A, left, right, k)
    else:
        left = index + 1
        return randomizedselection(A, left, right, k - index + left - 1)


inputArray = [7,4,6,9,0,2,5,3,1,8]
n = len(inputArray)
k = 4
if k > n:
    print("Please specify index less than array length")
    exit(0)
result = randomizedselection(inputArray, 0, n-1, k)
print(result)