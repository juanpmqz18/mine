# test_calculadora.py
import unittest
import math
from calculadora import *

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_log_base_10(self):
        self.assertAlmostEqual(log_base_10(100), 2)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_combinatoria(self):
        self.assertEqual(combinatoria(5, 2), 10)

    def test_inverso(self):
        self.assertEqual(inverso(2), 0.5)
        with self.assertRaises(ValueError):
            inverso(0)

if __name__ == '__main__':
    unittest.main()
