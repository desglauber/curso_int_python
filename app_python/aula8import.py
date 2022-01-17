from aula7tv import Televisao
from aula7 import Calculadora
from aula8contaletras import conta_letas, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = conta_letas(lista)
    print('O total de letras da lista é: {}'.format(total_letras))
    print(teste())