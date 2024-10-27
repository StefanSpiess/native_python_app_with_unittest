'''Module is gonna test our Fibonacci Solutions class'''

import time
import unittest

from unittesting_efficiency import FibonacciSequence

class EfficiencyTestCase(unittest.TestCase):
    '''Easy Tests'''

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = {}
        self._result_data = {}
        self._n = 30


    def test_recursive_method(self):
        '''Testing the recursive method'''
        starting_time = time.time()

        recursive_result = self._fibonacci_sequence.recursive_method(self._n)

        ending_time = time.time()

        self._result_data["recursive_method"] = f"Recursive method had result: {recursive_result}"
        self._efficiency_data["recursive_method"] = f"Recursive method took: {ending_time - starting_time}"

    def test_mathematical_method(self):
        '''Testing the mathematical method'''
        starting_time = time.time()

        math_result = self._fibonacci_sequence.math_method(self._n)

        ending_time = time.time()

        self._result_data["math_method"] = f"Math test had result: {math_result}"
        self._efficiency_data["math_method"] = f"Math test took: {ending_time - starting_time}"

    def tearDown(self):
        print(self._efficiency_data)
        print(self._result_data)
        self._fibonacci_sequence = None