#Gerenciando e criando exceções customizadas com try, except, else e finally

lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except ArithmeticError:
    print('Erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando não ocorre uma exceção')

finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()
    print('Arquivo fechado')