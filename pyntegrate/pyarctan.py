import threading
from typing import List

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

class arg_struct:
    def __init__(self, arr, arg1, arg2, depth):
        self.arr = arr
        self.arg1 = arg1
        self.arg2 = arg2
        self.depth = depth

def isPrime(n) -> bool:
    if (n <= 1) or (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3) or (n % 5 == 0 and n != 5) or (n % 7 == 0 and n != 7):
        return False
    for j in range(11, int(n**(1/2))+2, 2):
        if n % j == 0:
            return False
    return True

def primes(n: int) -> int:
    prnt = 0
    total = 0
    for i in range(0, n):
        if isPrime(i):
            if prnt == 1:
                print(i)
            total = total + 1
    return total

def integrate(f, a, b, n=1000000):

    h = (b-a)/float(n);
    s = f(a) + f(b);

    for i in range(1, n, 2):
        s = s + 4 * f(a + i * h);
    for i in range(2, n-1, 2):
        s = s + 2 * f(a + i*h)

    return (s*h)/3.0

def arctan(x) -> float:
    return integrate(lambda x: 1.0/(1.0 + x*x), 0, x)

def arctan2(x, n) -> float:
    return integrate(lambda x: 1.0/(1.0 + x*x), 0, x, n)

def bubblesort(arr) -> List[any]:
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                temp = float(arr[j-1])
                arr[j-1] = float(arr[j])
                arr[j] = temp
    return arr

def bubblesort2(arr) -> List[any]:
    itemCount = len(arr)
    hasChanged = 1
    while hasChanged != 0:
        if itemCount <= 1: break
        hasChanged = 0
        itemCount = itemCount - 1
        for j in range(0, itemCount):
            if arr[j] > arr[j+1]:
                temp = float(arr[j])
                arr[j] = float(arr[j+1])
                arr[j+1] = temp
                hasChanged = 1
    return arr

def merge(left, right):
    if type(left) == arg_struct: left = left.arr
    if type(right) == arg_struct: right = right.arr
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def mergesort(m) -> List[any]:
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return list(merge(left, right))

def p_mergesort(argv) -> List[any]:
    arr = argv.arr
    depth = argv.depth

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    argv_t = arg_struct(arr[:middle], -1, -1, depth+1)
    argv_m = arg_struct(arr[middle:], -1, -1, depth+1)

    if depth >= 1:
        left = p_mergesort(argv_t)
        right = p_mergesort(argv_m)
        return list(merge(left, right))
    else:
        x = ThreadWithReturnValue(target=p_mergesort, args=(argv_t,))
        y = ThreadWithReturnValue(target=p_mergesort, args=(argv_m,))

        x.start()
        y.start()

        left = x.join()
        right = y.join()

        return list(merge(left, right))

def insertionsort(A) -> List[any]:
    for j in range(1, len(A)):
        i = j
        while i > 0 and A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            i = i - 1
    return A

def arr_swap(arr, a, b) -> None:
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(arr, low, high):
    pivot = arr[low]
    lastSmall = low
    for i in range(low+1, high):
        if(arr[i] < pivot):
            lastSmall += 1
            arr_swap(arr, lastSmall, i)
    arr_swap(arr, low, lastSmall)
    return lastSmall

def quicksort(arr, low, high) -> List[any]:
    if low < high:
        part = partition(arr, low, high)
        quicksort(arr, low, part)
        quicksort(arr, part+1, high)
    return arr

def p_quicksort(argv) -> List[any]:
    arr = argv.arr
    low = argv.arg1
    high = argv.arg2
    depth = argv.depth

    if low < high:
        part = partition(arr, low, high)

        argv_t = arg_struct(arr, low, part, depth+1)
        argv_m = arg_struct(arr, part+1, high, depth+1)

        if depth >= 1:
            p_quicksort(argv_t)
            p_quicksort(argv_m)
            return
        else:
            x = threading.Thread(target=p_quicksort, args=(argv_t,))
            y = threading.Thread(target=p_quicksort, args=(argv_m,))

            x.start()
            y.start()

            y.join()
            x.join()

        return arr

def bucketsort(arr) -> List[any]:
    N = len(arr)
    bins = 10
    N2 = int((1.0/bins)*N)
    B = [[] for i in range(N2)]

    for i in range(N):
        B[int(arr[i]/(bins*N))].append(arr[i])

    for i in range(N2):
        if len(B[i]) > 1:
            quicksort(B[i], 0, len(B[i]))

    i = 0
    for j in range(N2):
        if len(B[j]) > 0:
            for val in B[j]:
                arr[i] = val
                i += 1
    return arr
