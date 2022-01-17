# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é o primeiro valor: {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é o segundo valor: {}'.format(b))
# else:
#     print('O maior número é o terceiro valor: {}'.format(c))
# print('Fim do programa')

# #Verifica se o número é par ou ímpar
# a = int(input('Entre com um valor inteiro: '))
# rest = a % 2
#
# if rest == 0:
#     print('O número {a} é par'. format(a=a))
# else:
#     print('O número {a} é ímpar'. format(a=a))

# #Verifica se o número é par ou ímpar
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# rest_a = a % 2
# rest_b = b % 2
#
# if rest_a == 0 or not rest_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')

#Boletim
a = int(input('Digite a nota do 1º bimestre: '))
if a > 10:
    a = int(input('Você digitou um valor errado. Digite a nota do 1º bimestre: '))
b = int(input('Digite a nota do 2º bimestre: '))
if b > 10:
    b = int(input('Você digitou um valor errado. Digite a nota do 2º bimestre: '))
c = int(input('Digite a nota do 3º bimestre: '))
if c > 10:
    c = int(input('Você digitou um valor errado. Digite a nota do 3º bimestre: '))
d = int(input('Digite a nota do 4º bimestre: '))
if d > 10:
    d = int(input('Você digitou um valor errado. Digite a nota do 4º bimestre: '))
media = ((a+b+c+d)/4)

print('A média do aluno é: {}'.format(media))