#Métodos e funções
#Função é tudo o que retorna valor
#Método não retorna valor
#No Python o método chama-se definição (def)

#Método de soma

class Calculadora:
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()

print('A soma é: ', calculadora.soma(10, 2))
print('A subtração é é: ', calculadora.subtracao(5, 3))
print('A multiplicação é: ', calculadora.multiplicacao(10, 5))
print('A divisão é: ', calculadora.divisao(100, 2))