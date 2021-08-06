import time, unittest

import pyntegrate.pyarctan as pyarctan
import pyntegrate.arctan as arctan

def makeArrMin(n, seed=25):
    return arctan.makeArrMin(n)

def makeArr(n, seed=25):
    return makeArrMin(n, seed), makeArrMin(n, seed)

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
        a, b = makeArr(self.n)
        
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

if __name__ == '__main__':
    unittest.main()
