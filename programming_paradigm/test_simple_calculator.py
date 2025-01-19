#Import the unittest module and the SimpleCalculator class from simple_calculator.py.
import unittest
from simple_calculator import SimpleCalculator

class Test_SimpleCalculator(unittest.TestCase):
          def test_all(self):
              calc = SimpleCalculator()
              self.assertEqual(calc.add(1, 1), 2)
              self.assertEqual(calc.subtract(1, 1), 0)
              self.assertEqual(calc.multiply(1, 1), 1)
              self.assertEqual(calc.divide(1, 1), 1)
              self.assertIsNone(calc.divide(1, 0))


if __name__ == "__main__":
    unittest.main()