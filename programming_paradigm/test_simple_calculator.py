import unittest
from simple_calculator import SimpleCalculator  

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_subtract(self):
        result = subtract(7, 2)
        self.assertEqual(result, 5)

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_multiply(self):
        result = multiply(5, 3)
        self.assertEqual(result, 15)

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()


    def test_divide(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)
