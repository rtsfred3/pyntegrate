import time, unittest

import pyntegrate
import pyntegrate.pyarctan as pyarctan
import pyntegrate.arctan as arctan

def makeArrMin(n, seed=2):
    return arctan.makeArrMin(n, seed)

def makeArr(n, seed=2):
    return makeArrMin(n, seed), makeArrMin(n, seed)

class TestVersion(unittest.TestCase):
    def test_version(self):
        assert pyntegrate.version() == '1.3.6.dev11'

class TestArctanMethods(unittest.TestCase):
    def test_bubblesort(self):
        assert arctan.bubblesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_bubblesort2(self):
        assert arctan.bubblesort2([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_quicksort(self):
        assert arctan.quicksort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_p_quicksort(self):
        assert arctan.p_quicksort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_mergesort(self):
        assert arctan.mergesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_p_mergesort(self):
        assert arctan.p_mergesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_insertionsort(self):
        assert arctan.insertionsort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    #def test_bucketsort(self):
    #    assert arctan.bucketsort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_ackermann(self):
        assert arctan.Ackermann(1, 10) == 12
        assert arctan.Ackermann(3, 10) == 8189
        assert arctan.Ackermann(4, 1) == 65533
        
    def test_ackermannLookup(self):
        assert arctan.AckermannLookup(1, 10) == 12
        assert arctan.AckermannLookup(3, 10) == 8189
        assert arctan.AckermannLookup(4, 1) == 65533
    
    def test_makeArrSequential(self):
        assert arctan.makeArrSequential(10) == [i for i in range(10)]
        assert arctan.makeArrSequential(100) == [i for i in range(100)]
        assert arctan.makeArrSequential(0) == []
        assert arctan.makeArrSequential(-1) == []
        assert arctan.makeArrSequential(-10) == []
        
    def test_makeArrZeroes(self):
        assert arctan.makeArrZeros(10) == [0 for i in range(10)]
        assert arctan.makeArrZeros(100) == [0 for i in range(100)]
        assert arctan.makeArrZeros(0) == []
        assert arctan.makeArrZeros(-1) == []
        assert arctan.makeArrZeros(-10) == []

class TestPyarctanMethods(unittest.TestCase):
    def setUp(self):
        self.inputArr = [4, 2, 3, 1]
        self.outputArr = [1, 2, 3, 4]
    
    def test_bubblesort(self):
        assert pyarctan.bubblesort(self.inputArr) == self.outputArr
    
    def test_bubblesort2(self):
        assert pyarctan.bubblesort2(self.inputArr) == self.outputArr
    
    def test_quicksort(self):
        assert pyarctan.quicksort(self.inputArr, 0, len(self.inputArr)) == self.outputArr
    
    def test_p_quicksort(self):
        assert pyarctan.p_quicksort(pyarctan.arg_struct(self.inputArr, 0, len(self.inputArr), 0)) == self.outputArr
    
    def test_mergesort(self):
        assert pyarctan.mergesort(self.inputArr) == self.outputArr
    
    def test_p_mergesort(self):
        assert pyarctan.p_mergesort(pyarctan.arg_struct(self.inputArr, 0, len(self.inputArr), 0)) == self.outputArr
    
    def test_insertionsort(self):
        assert pyarctan.insertionsort(self.inputArr) == self.outputArr
    
    #def test_bucketsort(self):
    #    assert pyarctan.bucketsort(self.inputArr) == self.outputArr

class TestTimeMethods(unittest.TestCase):
    def setUp(self):
        self.n = 100
    
    def test_bubblesort(self):
        a, b = makeArr(self.n, 2)
        
        startC = time.time()
        arctan.bubblesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.bubblesort(b)
        timePY = time.time() - startPY
        
        assert timeC < timePY
    
    def test_bubblesort2(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.bubblesort2(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.bubblesort2(b)
        timePY = time.time() - startPY
        
        assert timeC < timePY
    
    def test_quicksort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.quicksort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.quicksort(b, 0, len(b))
        timePY = time.time() - startPY
        
        assert timeC < timePY
    
    '''def test_p_quicksort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.p_quicksort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.p_quicksort(pyarctan.arg_struct(b, 0, len(b), 0))
        timePY = time.time() - startPY
        
        assert timeC < timePY'''

    def test_mergesort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.mergesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.mergesort(b)
        timePY = time.time() - startPY
        
        assert timeC < timePY

    '''def test_p_mergesort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.p_mergesort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.p_mergesort(pyarctan.arg_struct(b, 0, len(b), 0))
        timePY = time.time() - startPY
        
        assert timeC < timePY'''

    def test_insertionsort(self):
        a, b = makeArr(self.n)
        
        startC = time.time()
        arctan.insertionsort(a)
        timeC = time.time() - startC
        
        startPY = time.time()
        pyarctan.insertionsort(b)
        timePY = time.time() - startPY
        
        assert timeC < timePY
    
    def test_makeArrSequential(self):
        val = 1000000
        
        startC = time.time()
        a = arctan.makeArrSequential(val)
        timeC = time.time() - startC
        
        startPY = time.time()
        b = [i for i in range(val)]
        timePY = time.time() - startPY
        
        assert timeC < timePY

if __name__ == '__main__':
    unittest.main()
