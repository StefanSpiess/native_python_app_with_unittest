import unittest

from unittesting_average import calculate_average

class EasyTestCase(unittest.TestCase):

    def test_easy_one(self):
        self.assertEqual(calculate_average(1,2,3), 2)
    def test_easy_two(self):
        self.assertEqual(calculate_average(10,10,10), 10)
    def test_easy_three(self):
        self.assertEqual(calculate_average(1.5,1.5,3), 2)

class MediumTestCase(unittest.TestCase):

    def test_medium_one(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calculate_average(1,2,"Some String"), 2)
    def test_medium_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calculate_average(1,2,"3"), 2)

class HardTestCase(unittest.TestCase):

    def test_hard_one(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calculate_average(1,2,None), 2)
    def test_hard_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calculate_average(1,2,False), 2)
    def test_hard_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calculate_average(1,2,float), 2)
