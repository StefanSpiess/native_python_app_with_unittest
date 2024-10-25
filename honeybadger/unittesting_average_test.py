import unittest

from unittesting_average import average_of_integers

class EasyTestCase(unittest.TestCase):

    def test_easy_one(self):
        self.assertEqual(average_of_integers(1,2,3), 2)
    def test_easy_two(self):
        pass
    def test_easy_three(self):
        pass

class MediumTestCase(unittest.TestCase):

    def test_medium_one(self):
        with self.assertRaises(TypeError):
            self.assertEqual(average_of_integers(1,2,"Let's just go ahead and do this"), TypeError())
    def test_medium_two(self):
        pass
    def test_medium_three(self):
        pass