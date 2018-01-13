#!/usr/bin/python3

import unittest
from factorial import fact, div

class TestingFactorial(unittest.TestCase):
    '''
    A test class to test factorial.py specifically.
    '''

    def test_fact(self):
        '''
        The function which will perform test for factorial function.
        '''
        res = fact(4)
        self.assertEqual(res, 24)

    def test_div(self):
        '''
        The function which will perform test for division function.
        '''
        self.assertRaises(ZeroDivisionError, div(0))


if __name__ == '__main__':
    unittest.main()
