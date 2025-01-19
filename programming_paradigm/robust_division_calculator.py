import unittest
          
def safe_divide(numerator, denominator):

    try:
        # Convert input strings to float numbers
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
            
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"

class TestSafeDivide(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(10, 0), ZeroDivisionError)
        self.assertEqual(safe_divide(10, 'a'), ValueError)
        self.assertEqual(safe_divide('a', 2), ValueError)
        self.assertEqual(safe_divide('a', 'b'), ValueError)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)