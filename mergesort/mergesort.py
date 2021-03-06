"""
Algorithm:
----------
C = output array (length = n)
A = First sorted array (length = n/2)
B = Second sorted array (length = n/2)

set i = 1 and j = 1

for k = 1 to n
    if A[i] < B[j]
        C[k] = A[i]
        i++
    elif B[j] < A[i]
        C[k] = B[j]
        j++
end

Time complexity: O(nlog(n))
Space complexity: n
"""


def mergesort(array):
    if len(array) > 1:
        print("splitting: ", array)
        mid = len(array)//2
        first_half = array[:mid]
        second_half = array[mid:]

        mergesort(first_half)
        mergesort(second_half)

        i = 0
        j = 0
        k = 0

        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                array[k] = first_half[i]
                i += 1
            else:
                array[k] = second_half[j]
                j += 1
            k += 1

        while i < len(first_half):
            array[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            array[k] = second_half[j]
            j += 1
            k += 1

    print("merging: ", array)


arrayToSort = [5, 8, 2, 4, 1, 0, 6, 9, 3, 7]
mergesort(arrayToSort)