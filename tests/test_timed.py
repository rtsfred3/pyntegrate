import time, unittest, math

import pyntegrate
import pyntegrate.pyarctan as pyarctan
import pyntegrate.arctan as arctan

def makeArrMin(n, seed=2):
    return arctan.makeArrMin(n, seed)

def makeArr(n, seed=2):
    return makeArrMin(n, seed), makeArrMin(n, seed)

class TestTimeMethods(unittest.TestCase):
    def setUp(self):
        self.n = 100
        self.arrLength = 100000000
    
    def test_pi(self):
        startC = time.time()
        pi = arctan.pi()
        timeC = time.time() - startC

        print("test_pi")

        print(pi)
        print(math.pi)

        print("test_pi", round(timeC, 5))

    def test_bubblesort(self):
        a, b = makeArr(self.n, 2)
        
        startC = time.time()
        arctan.bubblesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.bubblesort(b)
        timePY = time.time() - startPY

        print("test_bubblesort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY
    
    def test_bubblesort2(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.bubblesort2(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.bubblesort2(b)
        timePY = time.time() - startPY

        print("test_bubblesort2", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY
    
    def test_quicksort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.quicksort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.quicksort(b, 0, len(b))
        timePY = time.time() - startPY

        print("test_quicksort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY

    def test_mergesort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.mergesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.mergesort(b)
        timePY = time.time() - startPY

        print("test_mergesort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY
    
    def test_p_quicksort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.p_quicksort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.p_quicksort(pyarctan.arg_struct(b, 0, len(b), 0))
        timePY = time.time() - startPY

        print("test_p_quicksort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY

    def test_p_mergesort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.p_mergesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.p_mergesort(pyarctan.arg_struct(b, 0, len(b), 0))
        timePY = time.time() - startPY

        print("test_p_mergesort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY

    def test_insertionsort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.insertionsort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.insertionsort(b)
        timePY = time.time() - startPY

        print("test_insertionsort", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY
    
    def test_makeArrSequential(self):
        startC = time.time()
        a = arctan.makeArrSequential(self.arrLength)
        timeC = time.time() - startC
        
        startPY = time.time()
        b = [i for i in range(self.arrLength)]
        timePY = time.time() - startPY

        print("test_makeArrSequential", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY
        
    def test_makeArrZero(self):
        startC = time.time()
        a = arctan.makeArrZeros(self.arrLength)
        timeC = time.time() - startC
        
        startPY = time.time()
        b = [0 for i in range(self.arrLength)]
        timePY = time.time() - startPY

        print("test_makeArrZero", round(timeC, 5), round(timePY, 5), round(timePY/timeC, 5))
        
        assert timeC < timePY

if __name__ == '__main__':
    unittest.main()
