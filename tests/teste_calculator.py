import unittest
from calculator import Calculator

class TestMinhaFuncao(unittest.TestCase):
    def test_soma(self):
        # Teste para verificar se a função somar está funcionando corretamente
        self.assertEqual(soma(1, 2), 3)  # Verifica se 1 + 2 = 3
        self.assertEqual(soma(-1, 1), 0)  # Verifica se -1 + 1 = 0
        self.assertEqual(soma(0, 0), 0)   # Verifica se 0 + 0 = 0x