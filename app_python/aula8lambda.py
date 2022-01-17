conta_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(conta_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
mult = lambda a, b: a * b
divisao = lambda a, b: a / b


print(soma(5, 10))
print(subtracao(10, 5))
print(mult(5, 10))
print(divisao(5, 10))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b
mult = calculadora['mult']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(mult(10, 2)))