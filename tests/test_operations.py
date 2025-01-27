import unittest
from complex_numbers.operations import *

class TestComplexOperations(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(suma((0, 0), (0, 0)), (0, 0))
    
    def test_resta(self):
        self.assertEqual(resta((5, 5), (2, 3)), (3, 2))
        self.assertEqual(resta((0, 0), (1, 1)), (-1, -1))

    def test_producto(self):
        self.assertEqual(producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(producto((0, 1), (1, 0)), (0, 1))
    
    def test_division(self):
        self.assertEqual(division((1, 2), (3, 4)), (0.44, 0.08))
        with self.assertRaises(ValueError):
            division((1, 1), (0, 0))

    def test_modulo(self):
        self.assertEqual(modulo((3, 4)), 5)
        self.assertEqual(modulo((0, 0)), 0)

    def test_conjugado(self):
        self.assertEqual(conjugado((3, 4)), (3, -4))
        self.assertEqual(conjugado((0, 0)), (0, 0))

    def test_conversion(self):
        self.assertEqual(cartesiano_a_polar((3, 4)), (5, math.atan2(4, 3)))
        self.assertEqual(polar_a_cartesiano((5, math.atan2(4, 3))), (3, 4))

    def test_fase(self):
        self.assertEqual(fase((3, 4)), math.atan2(4, 3))
        self.assertEqual(fase((0, 0)), 0)

if __name__ == '__main__':
    unittest.main()
