class Calculator:

    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b 

    def divisao(a, b):
       if b == 0:
           raise ValueError("Denominador não pode dividir por zero")
       return a / b

