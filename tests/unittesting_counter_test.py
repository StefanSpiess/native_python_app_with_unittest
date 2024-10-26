'''Module is gonna test our Counter class'''
import unittest

from unittesting_classes import Counter

class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_easy_one(self):
        self.assertEqual(self.counter.get_value(), 0)

    def test_easy_two(self):
        self.counter.increment()
        self.counter.increment()
        self.assertEqual(self.counter.get_value(), 2)

    def test_easy_three(self):
        self.counter.increment()
        self.counter.reset()
        self.assertEqual(self.counter.get_value(), 0)

    def tearDown(self):
        self.counter = None

class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_medium_one(self):
        pass

    def test_medium_two(self):
        pass

    def tearDown(self):
        self.counter = None

class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_hard_one(self):
        for _ in range(0, 1000):
            self.counter.increment()
        self.assertEqual(self.counter.get_value(), 1000)

    def tearDown(self):
        self.counter = None