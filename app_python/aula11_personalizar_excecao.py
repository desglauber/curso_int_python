class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota = int(input('Entre com uma nota de 0 a 10: '))
        print(nota)
        if nota > 10:
            raise InputError('A nota não pode ser maior que 10.')
        elif nota < 0:
            raise InputError('A nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido! Digite apenas números!')
    except InputError as ex:
        print(ex)