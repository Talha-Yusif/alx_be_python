import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
    
        self.calc = SimpleCalculator()

    def test_additin(self):
        self.assertEqual(self.calc.add(10,2), 12)
        self.assertEqual(self.calc.add(-10,-2), -12)
        self.assertEqual(self.calc.add(-10,2), -8)
        self.assertEqual(self.calc.add(0,0), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,2), 8)
        self.assertEqual(self.calc.subtract(-10,-2), -8)
        self.assertEqual(self.calc.subtract(10,-2), 12)
        self.assertEqual(self.calc.subtract(0,0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10,2), 20)
        self.assertEqual(self.calc.multiply(-10,-2), 20)
        self.assertEqual(self.calc.multiply(10,-2), -20)
        self.assertEqual(self.calc.multiply(-10,2), -20)
        self.assertEqual(self.calc.multiply(0,0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertEqual(self.calc.divide(-10,2), -5)
        self.assertEqual(self.calc.divide(10,-2), -5)
        self.assertEqual(self.calc.divide(16,5),3.2 )

        with self.assertRaises(ZeroDivisionError):

            self.calc.divide(10,0)

if __name__=="__main":
    unittest.main()


