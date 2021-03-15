import re, sys, time, random
import arctan, pyarctan
from help import *

def compute_prime(n):
    print("Computing Primes Up to %s\n" % ('{:,}'.format(n)))
    start = time.time()
    a = arctan.primes(n)
    t1 = time.time() - start
    printTime2("Non-Parallel C", t1, "\t ")
    
    start = time.time()
    p = arctan.p_primes(n)
    t3 = time.time() - start
    printTime2("Parallel C", t3, "\t ")

    start = time.time()
    b = pyarctan.primes(n)
    t2 = time.time() - start
    printTime2("Non-Parallel Py", t2, " ")

    print()

    print("({a} == {b}) = {c}".format(a=a, b=b, c=(b==a)))

    if t3 > 0: print("Parallel C is %0.3f times faster than Non-Parallel Python" % (t2/t3))
    if t1 > 0: print("Non-Parallel C is %0.3f times faster than Non-Parallel Python" % (t2/t1))

    if t3 > 0: print("\nParallel C is %0.3f times faster than Non-Parallel C" % (t1/t3))

def compute_prime_p(n):
    print("Computing Primes Up to %s\n" % ('{:,}'.format(n)))
    start = time.time()
    a = arctan.primes(n)
    t1 = time.time() - start
    printTime2("Non-Parallel C", t1, "\t ")

    start = time.time()
    p = arctan.p_primes(n)
    t2 = time.time() - start
    printTime2("Parallel C", t2, "\t ")

    print()

    print("({a} == {b}) = {c}".format(a=a, b=p, c=(p==a)))

    if t2 > 0: print("Parallel C is %0.3f times faster than Non-Parallel C" % (t1/t2))

def compute_arctan(n):
    print("arctan")
    start = time.time()
    print(4*arctan.arctan2(1.0, n))
    totalTimeC = round(time.time() - start, 6)
    print("C:", str(totalTimeC) + " seconds")

    print()

    start = time.time()
    print(4*pyarctan.arctan2(1.0, n))
    totalTimePython = round(time.time() - start, 6)
    print("Python:", str(totalTimePython) + " seconds")

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)

def compute_bubblesort(n):
    printHeading('Bubble Sort', n)
    a, b = makeArr(n)

    start = time.time()
    arctan.bubblesort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    pyarctan.bubblesort(b)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_bubblesort2(n):
    printHeading('Bubble Sort 2', n)
    a, b = makeArr(n, 100)

    start = time.time()
    arctan.bubblesort2(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    pyarctan.bubblesort2(b)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_quicksort(n):
    printHeading('Quick Sort', n)
    a, b = makeArr(n, 100)

    start = time.time()
    arctan.quicksort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    pyarctan.quicksort(b, 0, len(b))
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_p_quicksort(n):
    printHeading('Parallel Quick Sort', n)
    a, b = makeArr(n, 100)

    start = time.time()
    arctan.p_quicksort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    args = pyarctan.arg_struct(b, 0, len(b), 0)

    start = time.time()
    pyarctan.p_quicksort(args)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_p_mergesort(n):
    printHeading('Parallel Merge Sort', n)
    a, b = makeArr(n, 100)

    start = time.time()
    arctan.p_mergesort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    args = pyarctan.arg_struct(b, 0, len(b), 0)

    start = time.time()
    b = pyarctan.p_mergesort(args)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_merge_test(n):
    printHeading('Merge Sort Test', n)
    a, b = makeArr(n, 100)
    c, d = makeArr(n, 100)

    t = [0, 0, 0, 0] #[ Parallel C, Parallel Py, Non-Parallel C, Non-Parallel Py ]

    start = time.time()
    arctan.p_mergesort(a)
    t[0] = round(time.time() - start, 5)
    printTime2('[C]  Parallel', t[0])

    a = [int(i) for i in a]

    args = pyarctan.arg_struct(b, 0, len(b), 0)

    start = time.time()
    b = pyarctan.p_mergesort(args)
    t[1] = round(time.time() - start, 5)
    printTime2('[Py] Parallel', t[1])

    start = time.time()
    arctan.mergesort(c)
    t[2] = round(time.time() - start, 5)
    printTime2('[C]\tNon-P', t[2])

    c = [int(i) for i in c]

    start = time.time()
    d = pyarctan.mergesort(d)
    t[3] = round(time.time() - start, 5)
    printTime2('[Py]\tNon-P', t[3])

    print()

    print("P Merge Sort is %0.3f times faster than Merge Sort in C" % (t[2]/t[0]))
    print("P Merge Sort is %0.3f times faster than Merge Sort in Py" % (t[3]/t[1]))

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')
    print('`c` is sorted' if isSorted(c) else '`c` is not sorted')
    print('`d` is sorted' if isSorted(d) else '`d` is not sorted')

def compute_bucketsort(n):
    printHeading('Bucket Sort', n)
    a, b = makeArr(n, 100)
    #a, b = makeArrLin(n), makeArrLin(n)

    start = time.time()
    arctan.bucketsort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    pyarctan.bucketsort(b)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_b_v_b2_C(n):
    printHeading('Bubble Sort vs Bubble Sort 2 in C', n)
    #print('Bubble Sort vs Bubble Sort 2 in C: ' + '{:,}'.format(n) + "\n")
    a, b = makeArr(n)

    start = time.time()
    arctan.bubblesort(a)
    totalTimeB = round(time.time() - start, 5)
    printTime2('Bubble Sort', totalTimeB)

    a = [int(i) for i in a]

    start = time.time()
    arctan.bubblesort2(b)
    totalTimeB2 = round(time.time() - start, 5)
    printTime2('Bubble Sort 2', totalTimeB2)

    print()

    if totalTimeB2 > 0: print('Bubble Sort 2 is', round(totalTimeB/totalTimeB2, 5), 'times faster than Bubble Sort in C')

def compute_b_v_b2_P(n):
    printHeading('Bubble Sort vs Bubble Sort 2 in Py', n)
    a, b = makeArr(n)

    start = time.time()
    pyarctan.bubblesort(a)
    totalTimeB = round(time.time() - start, 5)
    printTime2('Bubble Sort', totalTimeB)

    a = [int(i) for i in a]

    start = time.time()
    pyarctan.bubblesort2(b)
    totalTimeB2 = round(time.time() - start, 5)
    printTime2('Bubble Sort 2', totalTimeB2)

    print()

    if totalTimeB2 > 0: print('Bubble Sort 2 is', round(totalTimeB/totalTimeB2, 5), 'times faster than Bubble Sort in Python')

def compute_mergesort(n):
    printHeading('Merge Sort', n)
    a, b = makeArr(n)

    start = time.time()
    arctan.mergesort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    b = pyarctan.mergesort(b)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def compute_insertsort(n):
    printHeading('Insertion Sort', n)
    a, b = makeArr(n)

    start = time.time()
    arctan.insertionsort(a)
    totalTimeC = round(time.time() - start, 5)
    printTime2('C', totalTimeC)

    a = [int(i) for i in a]

    start = time.time()
    b = pyarctan.insertionsort(b)
    totalTimePython = round(time.time() - start, 5)
    printTime2('Python', totalTimePython)

    print()

    if totalTimeC > 0: printTime(totalTimePython/totalTimeC)
    #printArr(a, 10)

    print('`a` is sorted' if isSorted(a) else '`a` is not sorted')
    print('`b` is sorted' if isSorted(b) else '`b` is not sorted')

def main(argv):
    if len(argv) == 1 and (argv[0] == '-h' or argv[0] == '--help') or ('-h' in argv or '--help' in argv):
        a = help()
        a.add('--primes=<num>', None, None, 'Computes Primes up to `n` in C & Python')
        a.add('--primesC=<num>', None, None, 'Computes Primes up to `n` in C')
        a.add('--primesP=<num>', None, None, 'Computes Primes up to `n` in Python')

        a.add('--bubble=<num>', None, None, 'Executes `Bubble Sort` in C & Python')
        a.add('--bubbleC=<num>', None, None, 'Executes `Bubble Sort` in C')
        a.add('--bubbleP=<num>', None, None, 'Executes `Bubble Sort` in Python')

        a.add('--bubble2=<num>', None, None, 'Executes `Bubble Sort 2` in C & Python')
        a.add('--bubble2C=<num>', None, None, 'Executes `Bubble Sort 2` in C')
        a.add('--bubble2P=<num>', None, None, 'Executes `Bubble Sort 2` in Python')

        a.add('--bubble_test=<num>', None, None, 'Executes `Bubble Sort 2` in C & Python')
        a.add('--bubble_testC=<num>', None, None, 'Executes `Bubble Sort 2` in C')
        a.add('--bubble_testP=<num>', None, None, 'Executes `Bubble Sort 2` in Python')

        a.add('--merge=<num>', None, None, 'Executes `Merge Sort` in C & Python')
        a.add('--mergeC=<num>', None, None, 'Executes `Merge Sort` in C')
        a.add('--mergeP=<num>', None, None, 'Executes `Merge Sort` in Python')

        a.add('--merge_p=<num>', None, None, 'Executes `Merge Sort` in C & Python')
        a.add('--merge_pC=<num>', None, None, 'Executes `Merge Sort` in C')
        a.add('--merge_pP=<num>', None, None, 'Executes `Merge Sort` in Python')

        a.add('--quick=<num>', None, None, 'Executes `Quick Sort` in C & Python')
        a.add('--quickC=<num>', None, None, 'Executes `Quick Sort` in C')
        a.add('--quickP=<num>', None, None, 'Executes `Quick Sort` in Python')

        a.add('--quick_p=<num>', None, None, 'Executes `Parallel Quick Sort` in C & Python')
        a.add('--quick_pC=<num>', None, None, 'Executes `Parallel Quick Sort` in C')
        a.add('--quick_pP=<num>', None, None, 'Executes `Parallel Quick Sort` in Python')

        a.add('--insert=<num>', None, None, 'Executes `Insertion Sort` in C & Python')
        a.add('--insertC=<num>', None, None, 'Executes `Insertion Sort` in C')
        a.add('--insertP=<num>', None, None, 'Executes `Insertion Sort` in Python')

        a.add('--bucket=<num>', None, None, 'Executes `Bucket Sort` in C & Python')
        a.add('--bucketC=<num>', None, None, 'Executes `Bucket Sort` in C')
        a.add('--bucketP=<num>', None, None, 'Executes `Bucket Sort` in Python')

        a.add('--merge_test=<num>', None, None, 'Compares `P Merge Sort` & `Merge Sort`')

        #a.add('--all', '[--bubble] [--bubble2] [--merge] [--quick] [--insert] [--bucket]', '--n=<num>', 'Executes `Bucket Sort` in Python')

        print(a)
        return

    verbose, pause = False, False

    t_arr = []

    if '-v' in argv:
        verbose = True
        argv.remove('-v')
    if '-p' in argv:
        pause = True
        argv.remove('-p')

    if '-array' in argv or '--array' in argv:
        n = 1000000
        s = time.time()
        a = arctan.makeArrMin(n)
        t1 = time.time() - s
        print(round(t1, 3), "seconds for C")

        s = time.time()
        b = makeArrMin(n)
        t2 = time.time() - s
        print(round(t2, 3), "seconds for Python")

        print("C is " + str(round(t2/t1, 3)) + " times faster than Python")

        #print(a)
        #print(arctan.makeArrMin(n))

        return

    #print(argv)
    for i in range(0, len(argv)):
        try:
            if argv[i] == '--all' and argv[i+1][0] == '-':
                pass
            elif argv[i] == '--all' and not (argv[i+1][0] == '-'):
                nn = int(argv[i+1])
            elif '=' in argv[i]:
                pass
            else:
                continue
        except:
            continue

        if "--prime=" in argv[i] or "--primes=" in argv[i]:
            nn = getN(argv[i])
            compute_prime(nn)
        if "--primeC=" in argv[i] or "--primesC=" in argv[i]:
            nn = getN(argv[i])
            if verbose:
                compute_prime_p(nn)
            else:
                arctan.primes(nn)
        if "--primeP=" in argv[i] or "--primesP=" in argv[i]:
            nn = getN(argv[i])
            if verbose:
                start = time.time()
                pyarctan.primes(nn)
                totalTime = time.time() - start
                print("[Py] Checked for prime numbers up {:,} in {:8.5f} seconds".format(nn, totalTime))
            else:
                pyarctan.primes(nn)

        if argv[i] == '-t':
            #nn = int(argv[i+1])
            if verbose:
                a = makeArrMin(nn)
                start = time.time()
                arctan.pass_arr(a)
                totalTime = round(time.time() - start, 5)
                if nn >= 10000000:
                    print("Array of length %s elements took\t%0.5f seconds" % ('{:,}'.format(nn), totalTime))
                else:
                    print("Array of length %s elements took\t\t%0.5f seconds" % ('{:,}'.format(nn), totalTime))

                #printArr(a, 10)
            else:
                a = makeArrMin(nn)
                arctan.pass_arr(a)

        if '--bubble=' in argv[i]:
            nn = getN(argv[i])
            compute_bubblesort(nn)
        if '--bubbleC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.bubblesort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bubble Sort", nn, "C", totalTime)
            else:
                arctan.bubblesort(a)
        if '--bubbleP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.bubblesort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bubble Sort", nn, "Py", totalTime)
            else:
                pyarctan.bubblesort(a)

        if '--bubble2=' in argv[i]:
            nn = getN(argv[i])
            compute_bubblesort2(nn)
        if '--bubble2C=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.bubblesort2(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bubble Sort 2", nn, "C", totalTime)
            else:
                arctan.bubblesort2(a)
        if '--bubble2P=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.bubblesort2(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bubble Sort 2", nn, "Py", totalTime)
            else:
                pyarctan.bubblesort2(a)

        if '--bubble_test=' in argv[i]:
            nn = getN(argv[i])
            compute_b_v_b2_C(nn)
            print()
            compute_b_v_b2_P(nn)
        if '--bubble_testC=' in argv[i]:
            nn = getN(argv[i])
            compute_b_v_b2_C(nn)
        if '--bubble_testP=' in argv[i]:
            nn = getN(argv[i])
            compute_b_v_b2_P(nn)

        if '--merge=' in argv[i]:
            nn = getN(argv[i])
            compute_mergesort(nn)
        if '--mergeC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.mergesort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Merge Sort", nn, "C", totalTime)
            else:
                arctan.mergesort(a)
        if '--mergeP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.mergesort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Merge Sort", nn, "Py", totalTime)
            else:
                pyarctan.mergesort(a)

        if '--merge_p=' in argv[i]:
            nn = getN(argv[i])
            compute_p_mergesort(nn)
        if '--merge_pC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.p_mergesort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("P Merge Sort", nn, "C", totalTime)
            else:
                arctan.p_mergesort(a)
        if '--merge_pP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            args = pyarctan.arg_struct(a, -1, -1, 0)
            if verbose:
                start = time.time()
                a = pyarctan.p_mergesort(args)
                totalTime = round(time.time() - start, 5)
                printSortTime("P Merge Sort", nn, "Py", totalTime)
            else:
                pyarctan.p_mergesort(args)

        if '--merge_test=' in argv[i]:
            nn = getN(argv[i])
            compute_merge_test(nn)

        if '--quick_p=' in argv[i]:
            nn = getN(argv[i])
            compute_p_quicksort(nn)
        if '--quick_pC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.p_quicksort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("P Quick Sort", nn, "C", totalTime)
            else:
                arctan.p_quicksort(a)
        if '--quick_pP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            args = pyarctan.arg_struct(a, 0, len(a), 0)
            if verbose:
                start = time.time()
                pyarctan.p_quicksort(args)
                totalTime = round(time.time() - start, 5)
                printSortTime("P Quick Sort", nn, "Py", totalTime)
            else:
                pyarctan.p_mergesort(args)

        if '-qmC=' in argv[i] or '-mqC=' in argv[i]:
            nn = getN(argv[i])
            a, b = makeArrMin(nn), makeArrMin(nn)
            time_arr = [0, 0] #[QuickSort, MergeSort]
            if verbose:
                start = time.time()
                arctan.quicksort(a)
                time_arr[0] = time.time() - start

                start = time.time()
                arctan.mergesort(a)
                time_arr[1] = time.time() - start

                printSortTime("Quick Sort", nn, "C", time_arr[0])
                printSortTime("Merge Sort", nn, "C", time_arr[1])

                print('\nQuick Sort is %0.3f times faster than Merge Sort in C for %s elements' % (time_arr[1]/time_arr[0], '{:,}'.format(nn)))

        if '-qm_pC=' in argv[i] or '-mq_pC=' in argv[i]:
            nn = getN(argv[i])
            a, b = makeArrMin(nn), makeArrMin(nn)
            time_arr = [0, 0] #[QuickSort, MergeSort]
            if verbose:
                start = time.time()
                arctan.p_quicksort(a)
                time_arr[0] = time.time() - start

                start = time.time()
                arctan.p_mergesort(a)
                time_arr[1] = time.time() - start

                printSortTime("P Quick Sort", nn, "C", time_arr[0])
                printSortTime("P Merge Sort", nn, "C", time_arr[1])

                print('\nP Quick Sort is %0.3f times faster than P Merge Sort in C for %s elements' % (time_arr[1]/time_arr[0], '{:,}'.format(nn)))

        if '--insert=' in argv[i]:
            nn = getN(argv[i])
            compute_insertsort(nn)
        if '--insertC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.insertionsort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Insertion Sort", nn, "C", totalTime)
            else:
                arctan.insertionsort(a)
        if '--insertP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.insertionsort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Insertion Sort", nn, "Py", totalTime)
            else:
                pyarctan.insertionsort(a)

        if '--quick=' in argv[i]:
            nn = getN(argv[i])
            compute_quicksort(nn)
        if '--quickC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                arctan.quicksort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Quick Sort", nn, "C", totalTime)
            else:
                arctan.quicksort(a)
        if '--quickP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.quicksort(a, 0, len(a))
                totalTime = round(time.time() - start, 5)
                printSortTime("Quick Sort", nn, "Py", totalTime)
            else:
                pyarctan.quicksort(a, 0, len(a))

        if '--bucket=' in argv[i]:
            nn = getN(argv[i])
            compute_bucketsort(nn)
        if '--bucketC=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn, time.time())
            if verbose:
                start = time.time()
                arctan.bucketsort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bucket Sort", nn, "C", totalTime)
                #printSorted(a)
            else:
                arctan.bucketsort(a)
            a = []
            del a
        if '--bucketP=' in argv[i]:
            nn = getN(argv[i])
            a = makeArrMin(nn)
            if verbose:
                start = time.time()
                pyarctan.bucketsort(a)
                totalTime = round(time.time() - start, 5)
                printSortTime("Bucket Sort", nn, "Py", totalTime)
                #printSorted(a)
            else:
                pyarctan.bucketsort(a)

        if argv[i] == '--all':
            runBubble, runBucket, runInsert, runQuick, runMerge, _all = False, False, False, False, False, False
            numTests = 12

            nn = -1

            if argv[i+1][0] == '-' and argv[i+1][1] == '-':
                for t in range(i+1, len(argv), 1):
                    if argv[t] == '--a':
                        runBubble, runBucket, runInsert, runQuick, runMerge, _all = True, True, True, True, True, True
                    if argv[t] == '--bubble':
                        runBubble = True
                    elif argv[t] == '--bucket':
                        runBucket = True
                    elif argv[t] == '--insert':
                        runInsert = True
                    elif argv[t] == '--quick':
                        runQuick = True
                    elif argv[t] == '--merge':
                        runMerge = True
                    elif '--n=' in argv[t] and argv[t][:4] == '--n=':
                        nn = getN(argv[t])
                if nn == -1: nn = int(argv[t+1])
            else:
                nn = int(argv[i+1])

            arrs = [list(makeArrMin(nn)) for i in range(numTests+1)]
            totalTimes = [0 for i in range(numTests)]

            #Default Sorted Algo
            start = time.time()
            sorted(arrs[-1])
            defaultTime = round(time.time() - start, 5)
            printSortTime("Default Sort", nn, "Py", defaultTime)

            if runMerge:
                print()

                #Merge Sort in C
                start = time.time()
                arctan.mergesort(arrs[0])
                totalTimes[0] = round(time.time() - start, 5)
                printSortTime("Merge Sort", nn, "C", totalTimes[0])

                #Merge Sort in Py
                start = time.time()
                pyarctan.mergesort(arrs[1])
                totalTimes[1] = round(time.time() - start, 5)
                printSortTime("Merge Sort", nn, "Py", totalTimes[1])

            if runQuick:
                print()

                #Quick Sort in C
                start = time.time()
                arctan.quicksort(arrs[2])
                totalTimes[2] = round(time.time() - start, 5)
                printSortTime("Quick Sort", nn, "C", totalTimes[2])

                #Quick Sort in Py
                start = time.time()
                pyarctan.quicksort(arrs[3], 0, len(arrs[3]))
                totalTimes[3] = round(time.time() - start, 5)
                printSortTime("Quick Sort", nn, "Py", totalTimes[3])

            if runInsert:
                print()

                #Insertion Sort in C
                start = time.time()
                arctan.insertionsort(arrs[4])
                totalTimes[4] = round(time.time() - start, 5)
                printSortTime("Insertion Sort", nn, "C", totalTimes[4])

                #Insertion Sort in Py
                start = time.time()
                pyarctan.insertionsort(arrs[5])
                totalTimes[5] = round(time.time() - start, 5)
                printSortTime("Insertion Sort", nn, "Py", totalTimes[5])

            if runBubble:
                print()

                #Bubble Sort in C
                start = time.time()
                arctan.bubblesort(arrs[6])
                totalTimes[6] = round(time.time() - start, 5)
                printSortTime("Bubble Sort", nn, "C", totalTimes[6])

                #Bubble Sort in Py
                start = time.time()
                pyarctan.bubblesort(arrs[7])
                totalTimes[7] = round(time.time() - start, 5)
                printSortTime("Bubble Sort", nn, "Py", totalTimes[7])

                print()

                #Bubble Sort 2 in C
                start = time.time()
                arctan.bubblesort2(arrs[8])
                totalTimes[8] = round(time.time() - start, 5)
                printSortTime("Bubble Sort 2", nn, "C", totalTimes[8])

                #Bubble Sort 2 in Py
                start = time.time()
                pyarctan.bubblesort2(arrs[9])
                totalTimes[9] = round(time.time() - start, 5)
                printSortTime("Bubble Sort 2", nn, "Py", totalTimes[9])

            if runBucket:
                print()

                #Bucket Sort in C
                start = time.time()
                arctan.bucketsort(arrs[10])
                totalTimes[10] = round(time.time() - start, 5)
                printSortTime("Bucket Sort", nn, "C", totalTimes[10])

                #Bucket Sort in Py
                start = time.time()
                pyarctan.bucketsort(arrs[11])
                totalTimes[11] = round(time.time() - start, 5)
                printSortTime("Bucket Sort", nn, "Py", totalTimes[11])

            print()

            if totalTimes[0] > 0 and runMerge: print('Merge Sort \tin C is %7.3f times faster than in Python' % (totalTimes[1]/totalTimes[0]))
            if totalTimes[2] > 0 and runQuick: print('Quick Sort \tin C is %7.3f times faster than in Python' % (totalTimes[3]/totalTimes[2]))
            if totalTimes[4] > 0 and runInsert: print('Insertion Sort \tin C is %7.3f times faster than in Python' % (totalTimes[5]/totalTimes[4]))
            if totalTimes[6] > 0 and runBubble: print('Bubble Sort \tin C is %7.3f times faster than in Python' % (totalTimes[7]/totalTimes[6]))
            if totalTimes[8] > 0 and runBubble: print('Bubble Sort 2 \tin C is %7.3f times faster than in Python' % (totalTimes[9]/totalTimes[8]))
            if totalTimes[10] > 0 and runBucket: print('Bucket Sort \tin C is %7.3f times faster than in Python' % (totalTimes[11]/totalTimes[10]))

        if argv[i] == '-arc':
            compute_arctan(nn)
        if argv[i] == '-arcC':
            a = 4*arctan.arctan2(1.0, nn)
        if argv[i] == '-arcP':
            a = 4*pyarctan.arctan2(1.0, nn)

        if i < len(argv) - 1 and not ('--n=' in argv[i]): print()

    if pause: n = input('in')

if __name__== "__main__":
    main(sys.argv[1:])
    
    '''n = 750000000
    
    a, b = makeArr(n)
    
    start = time.time()
    arctan.isSorted(a)
    print(round(time.time() - start, 6), 's')
    
    start = time.time()
    isSorted(b)
    print(round(time.time() - start, 6), 's')'''