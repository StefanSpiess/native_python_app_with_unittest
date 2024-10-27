# -*- coding: utf-8 -*-
'''
Remember to run this without explicitely using unittest from commandline!
Explanation: There are two ways how you can execute this from the command line.

1. RECOMMENDED:
    python test_suite.py
2. NOT recommended:
    python -m unittest test_suite.py

Variant 1
Will respect your specified test suite.

Variant 2
Will trigger unittest default test detection behaviour
and execute all tests in all imported modules.
'''

import unittest
from unittesting_car_class_test import EasyTestCase
import HtmlTestRunner
from datetime import datetime

def test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(EasyTestCase("test_get_attribute"))
    return test_suite

if __name__ == "__main__":
    # Configure the HTMLTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        output='test_reports',  # Directory to store the report
        verbosity=2
    )

    # Run the test suite
    runner.run(test_suite())
