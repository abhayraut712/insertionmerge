import unittest
import random
from mergesorting import mergesort
from insertionsorting import insertionsort

number_of_test_cases=10000
class SearchTestCase(unittest.TestCase):

    def test_insertionsort(self):

        randomnum=random.sample(range(100000),number_of_test_cases)
        sortednum=sorted(randomnum)
        self.assertEqual(insertionsort(randomnum),sortednum)

    def test_mergesort(self):

        randomnum=random.sample(range(100000),number_of_test_cases)
        sortednum=sorted(randomnum)
        self.assertEqual(mergesort(randomnum),sortednum)

if __name__=='__main__':
    unittest.main()
