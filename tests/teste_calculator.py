import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_soma(self):
        self.calculator1 = Calculator(2, 3)
        self.calculator2 = Calculator(3, 4)
        self.calculator3 = Calculator(7, 10)

    def test_subtracao(self):
        self.calculator4 = Calculator(9, 13)
        self.calculator5 = Calculator(12, 31)
        self.calculator6 = Calculator(15, 20)

    def test_multiplicacao(self):
        self.calculator7 = Calculator(14, 8)
        self.calculator8 = Calculator(8, 9)
        self.calculator9 = Calculator(7, 5)

    def test_divisao(self):
        self.calculator = Calculator(12, 6)
        self.calculator = Calculator(25, 5)
        self.calculator = Calculator(35, 7)