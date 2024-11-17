import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
     def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

     def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # Simple addition
        self.assertEqual(self.calc.add(-2, -3), -5)  # Adding negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Adding zero
        self.assertEqual(self.calc.add(-2, 3), 1)  # Mixed sign numbers

     def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2) 
        self.assertEqual(self.calc.subtract(-5, -3), -2)  
        self.assertEqual(self.calc.subtract(0, 0), 0)  
        self.assertEqual(self.calc.subtract(3, -3), 6) 

     def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)  
        self.assertEqual(self.calc.multiply(-2, 3), -6)  
        self.assertEqual(self.calc.multiply(0, 5), 0)  
        self.assertEqual(self.calc.multiply(-2, -3), 6)  

     def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2) 
        self.assertEqual(self.calc.divide(-6, 3), -2)  
        self.assertEqual(self.calc.divide(0, 1), 0)  
        self.assertIsNone(self.calc.divide(6, 0))  
        self.assertAlmostEqual(self.calc.divide(7, 3), 7 / 3)     
   

if __name__ == '__main__':
    unittest.main()
        
   