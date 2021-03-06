# some array fun with a timer
from timer import Timer
import numpy as np
import copy
import itertools

def quicksort(input_array: np.array, lo: int, hi: int):
    if lo < hi:
        p = partition(input_array, lo, hi)
        quicksort(input_array, lo, p - 1)
        quicksort(input_array, p + 1, hi)

def partition(arr: np.array, lo: int, hi: int):
    i = (lo - 1)
    pivot = A[hi]
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return (i + 1)

def mergeSort(arr: np.array):
    if len(arr) > 1:
        mid = len(arr) // 2 # floor division by 2
        leftArr = arr[: mid]
        rightArr = arr[mid: ]

        # Sorting the first half
        mergeSort(leftArr)

        # Sorting the second half
        mergeSort(rightArr)

        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i+= 1
            else:
                arr[k] = rightArr[j]
                j+=1
            k += 1

        # check if any element was left
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

def integerToArray(inte: int):
    # xor for sign
    if inte < 0:
        sign = -1
    else:
        sign = 1
    inte = abs(inte)
    int_str = str(inte)
    len_str = len(int_str)
    arr = np.empty(len_str)
    for j in range(len_str):
        arr[j] =  int(int_str[j])
    arr = arr.astype(int)
    arr[0] *= sign

    return arr.tolist()

def arrayMultiplicator(arr1: np.array, arr2: np.array):
    """

    :type arr1: numpy array, arr2: numpy array
    """
    # xor for sign
    if arr1[0] < 0 ^ arr2[0] < 0:
        sign = -1
    else:
        sign = 1
    temp1 = 0
    temp2 = 0

    # since multiplication is commutative, swap arr1 and arr2 so that shorter one is arr2 make positive too

    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1

    # make positive
    arr1[0] = abs(arr1[0])
    arr2[0] = abs(arr2[0])

    for j in range(0, len(arr2)):
        for i in range(0, len(arr1)):
            temp1 += arr2[len(arr2) - 1 -j] * arr1[len(arr1) - 1 -i] * 10**(i+j)
        temp2+=temp1
        temp1 = 0
    return sign*temp2


if __name__ == '__main__':
    t = Timer()
    # test quicksort
    s_size = [100] # sample size
    arr_size = [10] #, 50, 100, 400, 800] # array size
    for crawler in itertools.product(s_size, arr_size):
        t.start()
        for j in range(crawler[0]):
            A = np.random.randint(100, size=crawler[1])
            quicksort(A, 0, len(A) - 1)
        t.stop()
        print("Quicksort |", s_size," Arrays of size", crawler[1], f" Elapsed time: {t._elapsed_time:0.4f} seconds")

    print(" ")

    for crawler in itertools.product(s_size, arr_size):
        t.start()
        for j in range(crawler[0]):
            A = np.random.randint(100, size=crawler[1])
            mergeSort(A)
        t.stop()
        print("Mergesort |", s_size," Arrays of size", crawler[1], f" Elapsed time: {t._elapsed_time:0.4f} seconds")

    # comparing inserting with appending

    n = 10000
    t.start()
    A = []
    for j in range(n):
        A = np.append(A, [j])
    t.stop()
    print(f" Append | Elapsed time: {t._elapsed_time:0.4f} seconds")

    append_time = t._elapsed_time

    t.start()
    A = np.empty((n,1))
    for j in range(n):
        A[j] = j
    t.stop()
    print(f" Insert | Elapsed time: {t._elapsed_time:0.4f} seconds")

    insert_time = t._elapsed_time

    print(" ")

    print(f" Insert takes only {insert_time/append_time*100:0.2f} % of the time that it takes to append.")

    # result of big multiplication
    print(" ")
    arr1 = integerToArray(21221)
    arr2 = integerToArray(5)
    print(f"Result of multiplying {arr1} with {arr2}:")
    print(arrayMultiplicator(arr1, arr2))
    # interestingly, buffer overflow when arrays are numpy arrays, not when they are stored as lists