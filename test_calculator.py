import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # Test case 1
        self.assertEqual(self.calc.add(-1, -5), -6)  # Test case 2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)  # Test case 1
        self.assertEqual(self.calc.subtract(0, 7), -7)  # Test case 2

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Test case 1
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Test case 2

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # Test case 1
        self.assertEqual(self.calc.divide(9, 3), 3)  # Test case 2

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # Test case 1
        self.assertEqual(self.calc.modulo(14, 5), 4)  # Test case 2

if __name__ == '__main__':
    unittest.main()