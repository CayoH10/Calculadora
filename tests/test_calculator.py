import unittest
from calculator import Calculator

class Test_Calculator(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(Calculator.soma(10, 5), 15)
        self.assertEqual(Calculator.soma(-1, 1), 0)
        self.assertEqual(Calculator.soma(12, 7), 21)
        self.assertEqual(Calculator.soma(14, 8), 15)

    def test_subtracao(self):
        self.assertEqual(Calculator.subtracao(10, 5), 15)
        self.assertEqual(Calculator.subtracao(-1, 1), 0)
        self.assertEqual(Calculator.subtracao(12, 7), 21)
        self.assertEqual(Calculator.subtracao(14, 8), 15)

    def test_multiplicacao(self):
        self.assertEqual(Calculator.multiplicacao(10, 5), 15)
        self.assertEqual(Calculator.multiplicacao(-1, 1), 0)
        self.assertEqual(Calculator.multiplicacao(12, 7), 21)
        self.assertEqual(Calculator.multiplicacao(14, 8), 15)

    def test_divisao(self):
        self.assertEqual(Calculator.divisao(10, 5), 15)
        self.assertEqual(Calculator.divisao(-1, 1), 0)
        self.assertEqual(Calculator.divisao(12, 7), 21)
        self.assertEqual(Calculator.divisao(14, 8), 15)

