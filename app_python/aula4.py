# for x in range(101):
#     print(x)

# #Verifica se o número é primo
#
# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     rest = a % x
#     print('O resto de {a} dividido por {x} é: {rest}'. format(a=a, x=x, rest=rest))
#     if rest == 0:
#         div += 1
#
# if div == 2:
#     print('O número {} é primo!'.format(a))
# else:
#     print('O número {} não é primo!'.format(a))

# #informa os números primos que estão no tamanho do valor informado usando o FOR
#
# a = int(input('Entre com o número: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         rest = num % x
#         #print(x, rest)
#         if rest == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

#usando o while para a média de uma nota

a = int(input('Digite a nota do 1º bimestre: '))
while a > 10:
    a = int(input('Você digitou a nota errada. Digite a nota do 1º bimestre: '))
b = int(input('Digite a nota do 2º bimestre: '))
while b > 10:
    b = int(input('Você digitou a nota errada. Digite a nota do 2º bimestre: '))
c = int(input('Digite a nota do 3º bimestre: '))
while c > 10:
    c = int(input('Você digitou a nota errada. Digite a nota do 3º bimestre: '))
d = int(input('Digite a nota do 4º bimestre: '))
while d > 10:
    d = int(input('Você digitou a nota errada. Digite a nota do 4º bimestre: '))
media = ((a+b+c+d)/4)

print('A média do aluno é: {}'.format(media))