'''Module is gonna test our Car class'''
#TODO: Correct class name in module docstring

import unittest

from unittesting_car_class import Car

class EasyTestCase(unittest.TestCase):
    '''Easy Tests'''

    def setUp(self):
        self.car = Car() #TODO: Correct class name

    def test_easy_one(self):
        '''TODO: DOCSTRING GOES HERE'''
        pass

    def tearDown(self):
        self.car = None #TODO: Correct class name

class MediumTestCase(unittest.TestCase):
    '''Medium Tests'''

    def setUp(self):
        self.car = Car() #TODO: Correct class name

    def test_medium_one(self):
        '''TODO: DOCSTRING GOES HERE'''
        pass

    def tearDown(self):
        self.car = None #TODO: Correct class name

class HardTestCase(unittest.TestCase):
    '''Hard Core Tests - And here we go shitting nuclear bricks into the engine.'''

    def setUp(self):
        self.car = Car() #TODO: Correct class name

    def test_hard_one(self):
        '''TODO: DOCSTRING GOES HERE'''
        pass

    def tearDown(self):
        self.car = None #TODO: Correct class name
