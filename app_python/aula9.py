# #cria um arquivo e escreve
# open('teste.txt', 'w')
#
# # abre/cria arquivo, escreve sobrepondo caso já tenha algo escrito no arquivo
# arquivo = open('teste.txt', 'w')
# arquivo.write('Segunda linha')
# arquivo.close()
#
# # abre/cria arquivo, escreve adicionando
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nSegunda linha')
# arquivo.close()

import shutil

#Métodos
def escrever_arquivo(texto):
    diretorio = 'f:/Projetos diversos/Python/teste.txt'
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

#Método para ler o conteúdo do arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',') #cria uma lista separando o conteúdo das vírgulas
        aluno = lista_notas[0] #cria uma lista com os nomes que estão na posição 0 da lista_notas
        lista_notas.pop(0) #remove a primeira posição da lista que é o nome, deixando apenas as notas bimestrais
        print(aluno)
        print(lista_notas)
        media = lambda notas : sum([int(i) for i in notas])/4 #transforma a lista em inteiros e calcula a média das notas
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'f:/Projetos diversos/Python/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'f:/Projetos diversos/Python/')

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Manoel,7,8,5,6\n'
    #atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
