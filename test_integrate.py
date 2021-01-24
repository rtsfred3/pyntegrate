import unittest
import arctan, pyarctan

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

if __name__ == '__main__':
    unittest.main()