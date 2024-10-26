import unittest

from unittesting_counter import count_letters

class EasyTestCase(unittest.TestCase):

    def test_easy_one(self):
        self.assertEqual(count_letters("Mohammad"), 8)
    def test_easy_two(self):
        self.assertEqual(count_letters("Mo"), 2)

class MediumTestCase(unittest.TestCase):

    def test_medium_one(self):
        with self.assertRaises(TypeError):
            self.assertEqual(count_letters("!Mohammad#"), 2)
    def test_medium_two(self):
        self.assertEqual(count_letters("Moham mad"), 8)

class HardTestCase(unittest.TestCase):

    def test_hard_one(self):
        with self.assertRaises(TypeError):
            self.assertEqual(count_letters(""), 2)
    def test_hard_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(count_letters(None), 2)
    def test_hard_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(count_letters(True), 2)