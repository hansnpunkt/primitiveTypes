# some array fun with a timer
from timer import Timer
import numpy as np

def quicksort(input_array: np.array, lo: int, hi: int):
    # move pivot to end of array
    if lo < hi:
        p = partition(input_array, lo, hi)
        quicksort(input_array, lo, p - 1)
        quicksort(input_array, p+1, hi)

def partition(arr: np.array, lo: int, hi: int):
    i = (lo - 1)
    pivot = A[hi]
    for j in range(lo,hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return (i + 1)

if __name__ == '__main__':
    t = Timer()

    t.start()
    A = np.random.randint(100, size=100)
    print(A)
    quicksort(A, 0, len(A)-1)
    print(A)
    t.stop()