import unittest
from unittesting_base import str_to_uppercase  # Import the function from the file you want to test

class TestStrToUppercase(unittest.TestCase):
    def test_str_to_uppercase(self):
        result = str_to_uppercase("Stefan Spiess")
        self.assertEqual(result, "STEFAN SPIESS")  # Replace with your expected output

if __name__ == '__main__':
    unittest.main()