#Import the unittest module and the SimpleCalculator class from simple_calculator.py.
import unittest
from simple_calculator import SimpleCalculator

class Test_SimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

        def test_addition(self):
          """Test the addition method."""
          self.assertEqual(self.calc.add(1, 1), 2)
          self.assertEqual(self.calc.add(-1, 1), 0)
                    
        def test_subtraction(self):
          """Test the subtract method."""
          self.assertEqual(self.calc.subtract(1, 1), 0)

        def test_multiplication(self):
          """Test the multiply method."""
          self.assertEqual(self.calc.multiply(1, 1), 1)

        def test_division(self):
          """Test the divide method."""
          self.assertEqual(self.calc.divide(1, 1), 1)
          self.assertIsNone(self.calc.divide(1, 0))

if __name__ == "__main__":
    unittest.main()