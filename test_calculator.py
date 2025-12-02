import unittest
from calculator import factorial

class TestFactorial(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
    
    def test_large(self):
        self.assertEqual(factorial(10), 3628800)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_non_int(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
    
    def test_string_input(self):
        with self.assertRaises(TypeError):
            factorial("5")

if __name__ == "__main__":
    unittest.main()