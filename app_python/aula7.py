#Métodos e funções
#Função é tudo o que retorna valor
#Método não retorna valor
#No Python o método chama-se definição (def)

#Método de soma

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    escolha = int(input('O que você deseja fazer? 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir'))

    num1 = int(input('Valor 1: '))
    num2 = int(input('Valor 2: '))

    calculadora = Calculadora(num1, num2)

    if escolha == 1:
        print('A soma é: ', calculadora.soma())

    elif escolha == 2:
        print('A subtração é: ', calculadora.subtracao())

    elif escolha == 3:
        print('A multiplicação é: ', calculadora.multiplicacao())

    else:
        print('A divisão é: ', calculadora.divisao())

    # print('A soma é: ', calculadora.soma())
    # print('A subtração é é: ', calculadora.subtracao())
    # print('A multiplicação é: ', calculadora.multiplicacao())
    # print('A divisão é: ', calculadora.divisao())