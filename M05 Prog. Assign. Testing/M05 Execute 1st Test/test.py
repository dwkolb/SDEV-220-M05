#SDEV 220    11/20/2023
#M05 Programming Assignment
#https://realpython.com/python-testing/#testing-your-code
#Writing Your First Test/ Executing Your First Test

from fractions import Fraction
import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def tests_list_int(self):
        '''
        Test that it can sum a list of integers
        '''
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)
    
if __name__ == "__main__":
    unittest.main()