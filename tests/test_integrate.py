import os, time, unittest

import pyntegrate
import pyntegrate.pyarctan as pyarctan
import pyntegrate.arctan as arctan

def makeArrMin(n, seed=2):
    return arctan.makeArrMin(n, seed)

def makeArr(n, seed=2):
    return makeArrMin(n, seed), makeArrMin(n, seed)

class TestArctanMethods(unittest.TestCase):
    def test_bubblesort(self):
        assert arctan.bubblesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_bubblesort2(self):
        assert arctan.bubblesort2([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_quicksort(self):
        assert arctan.quicksort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_mergesort(self):
        assert arctan.mergesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_insertionsort(self):
        assert arctan.insertionsort([4, 2, 3, 1]) == [1, 2, 3, 4]
        
    # def test_wilson(self):
    #     assert arctan.wilson(1) == 2
    #     assert arctan.wilson(2) == 3
    #     assert arctan.wilson(3) == 2
    #     assert arctan.wilson(4) == 5
    #     assert arctan.wilson(5) == 2
    #     assert arctan.wilson(6) == 7
    #     assert arctan.wilson(7) == 2
    #     assert arctan.wilson(8) == 2
    #     assert arctan.wilson(9) == 2
    
    # def test_isPrimeWilson(self):
    #     assert arctan.isPrimeWilson(2) == 1
    #     assert arctan.isPrimeWilson(3) == 1
    #     assert arctan.isPrimeWilson(4) == 0
    #     assert arctan.isPrimeWilson(5) == 1
    #     assert arctan.isPrimeWilson(6) == 0
    #     assert arctan.isPrimeWilson(7) == 1
    #     assert arctan.isPrimeWilson(8) == 0
    
    def test_willans(self):
        assert arctan.willans(1) == 2
        assert arctan.willans(2) == 3
        assert arctan.willans(3) == 5
        assert arctan.willans(4) == 7
        # assert arctan.willans(5) == 11
        # assert arctan.willans(6) == 13
        # assert arctan.willans(7) == 17
        # assert arctan.willans(8) == 19
    
    def test_p_quicksort(self):
        if os.name == 'posix': assert arctan.p_quicksort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    '''def test_p_mergesort(self):
        assert arctan.p_mergesort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_bucketsort(self):
        assert arctan.bucketsort([4, 2, 3, 1]) == [1, 2, 3, 4]
    
    def test_ackermann(self):
        assert arctan.Ackermann(1, 10) == 12
        assert arctan.Ackermann(3, 10) == 8189
        assert arctan.Ackermann(4, 1) == 65533
    
    def test_ackermannLookup(self):
        assert arctan.AckermannLookup(1, 10) == 12
        assert arctan.AckermannLookup(3, 10) == 8189
        assert arctan.AckermannLookup(4, 1) == 65533'''
    
    def test_makeArrSequential(self):
        assert arctan.makeArrSequential(10) == [i for i in range(10)]
        assert arctan.makeArrSequential(100) == [i for i in range(100)]
        assert arctan.makeArrSequential(0) == []
        assert arctan.makeArrSequential(-1) == []
        assert arctan.makeArrSequential(-10) == []
        
    def test_makeArrZeroes(self):
        assert arctan.makeArrZeros(5) == [0 for i in range(5)]
        assert arctan.makeArrZeros(10) == [0 for i in range(10)]
        assert arctan.makeArrZeros(15) == [0 for i in range(15)]
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
    
    def test_mergesort(self):
        assert pyarctan.mergesort(self.inputArr) == self.outputArr
    
    def test_insertionsort(self):
        assert pyarctan.insertionsort(self.inputArr) == self.outputArr
    
    '''def test_p_quicksort(self):
        assert pyarctan.p_quicksort(pyarctan.arg_struct(self.inputArr, 0, len(self.inputArr), 0)) == self.outputArr
    
    def test_p_mergesort(self):
        assert pyarctan.p_mergesort(pyarctan.arg_struct(self.inputArr, 0, len(self.inputArr), 0)) == self.outputArr
    
    def test_bucketsort(self):
       assert pyarctan.bucketsort(self.inputArr) == self.outputArr'''

if __name__ == '__main__':
    unittest.main()
