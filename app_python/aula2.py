a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
sum = a + b
sub = a - b
mult = a * b
div = a / b
rest = a % b
# print('Soma: ' + str(sum))
# print('Subtração: ' + str(sub))
# print('Multiplicação: ' + str(mult))
# print('Divisão: ' + str(div))
# print('Resto: ' + str(rest))
resultado = ('Soma: {sum}. \nSubtração: {sub}. '
       '\nMultiplicação: {mult} '
       '\nDivisão: {div}'
       '\nResto: {rest}'. format(sum=sum, sub=sub, mult=mult, div=div, rest=rest))
print(resultado)
