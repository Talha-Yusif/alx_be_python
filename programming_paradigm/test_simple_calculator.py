import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
    
        self.calc = SimpleCalculator()

    def test_additin(self):
        self.assertEqual(calc.add(10,2), 12)
        self.assertEqual(calc.add(-10,-2), -12)
        self.assertEqual(calc.add(-10,2), -8)
        self.assertEqual(calc.add(0,0), 0)
    
    def test_subtraction(self):
        self.assertEqual(calc.subtract(10,2), 8)
        self.assertEqual(calc.subtract(-10,-2), -8)
        self.assertEqual(calc.subtract(10,-2), 12)
        self.assertEqual(calc.subtract(0,0), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,2), 20)
        self.assertEqual(calc.multiply(-10,-2), 20)
        self.assertEqual(calc.multiply(10,-2), -20)
        self.assertEqual(calc.multiply(-10,2), -20)
        self.assertEqual(calc.multiply(0,0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10,2), 5)
        self.assertEqual(calc.divide(-10,2), -5)
        self.assertEqual(calc.divide(10,-2), -5)
        self.assertEqual(calc.divide(16,5),3.2 )

        with self.assertRaises(ZeroDivisionError):

            calc.divide(10,0)

if __name__=="__main":
    unittest.main()


