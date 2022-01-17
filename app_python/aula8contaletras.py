#Método que conta letras

def conta_letas(lista_palavras):
    contador = []
    for x in lista_palavras:
        qtd = len(x)
        contador.append(qtd)
    return contador

def teste():
    return 'testado'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(conta_letas(lista))