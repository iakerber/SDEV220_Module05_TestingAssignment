import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        This is a test that it can sum a list of integers
        """

        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)


    def test_list_fraction(self):
        """
        This is a test that it can sum a list of fractions
        """
        data = [.25, .25, .40]
        
        result = sum(data)
        self.assertEqual(result, 1)
        

if __name__== '__main__':
    unittest.main()
