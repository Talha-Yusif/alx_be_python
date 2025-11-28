import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10,2), 12)
        self.assertEqual(add(-10,-2), -12)
        self.assertEqual(add(-10,2), -8)
        self.assertEqual(add(0,0), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(10,2), 8)
        self.assertEqual(subtract(-10,-2), -8)
        self.assertEqual(subtract(10,-2), 12)
        self.assertEqual(subtract(0,0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10,2), 20)
        self.assertEqual(multiply(-10,-2), 20)
        self.assertEqual(multiply(10,-2), -20)
        self.assertEqual(multiply(-10,2), -20)
        self.assertEqual(multiply(0,0), 0)

    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(-10,2), -5)
        self.assertEqual(divide(10,-2), -5)
        self.assertEqual(divide(16,5),3.2 )

        with self.assertRaises(ZeroDivisionError):

            divide(10,0)

if __name__=="__main":
    unittest.main()


