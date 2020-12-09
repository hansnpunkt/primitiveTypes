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


if __name__ == '__main__':
    t = Timer()
    # test quicksort
    s_size = [100] # sample size
    arr_size = [10, 50, 100, 400, 800] # array size
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
