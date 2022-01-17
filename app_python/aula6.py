#Conjuntos "Set" o conteúdo não se repete

# conjunto = {1, 2, 3, 4}
# print('O tipo de classe é; ', type(conjunto))
# print('O conjunto é: ', conjunto)
# conjunto.add(int(input('Adicione um valor ao conjunto: ')))
# print(conjunto)
# conjunto.discard(int(input('Escolha um valor do conjunto para descartar: ')))
# print(conjunto)

#união de conjuntos
# conjunto1 = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjuntos = conjunto1.union(conjunto2)
# print('A união dos conjuntos é: ', conjuntos)
# print('A intercecção dos conjuntos é: ', conjunto1.intersection(conjunto2))
# print('A diferença do conjunto 1 para o 2 é: ', conjunto1.difference(conjunto2))
# print('A diferença do conjunto 2 para o 1 é: ', conjunto2.difference(conjunto1))
# print('A diferença simétrica do conjunto 1 para o 2 é: ', conjunto1.symmetric_difference(conjunto2))

#Subconjuntos
# conjuntoa = {1, 2, 3}
# conjuntob = {1, 2, 3, 4, 5}
# print('O conjunto a é subconjunto do b: ', conjuntoa.issubset(conjuntob))
# print('O conjunto b é subconjunto do a: ', conjuntob.issubset(conjuntoa))
# print('O conjunto b é um superconjunto do a: ', conjuntob.issuperset(conjuntoa))
# print('O conjunto a é um superconjunto do b: ', conjuntoa.issuperset(conjuntob))

#Transformando conjunto em lista (Remove duplicidade)
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjuntoanimais = set(lista)
print('O conjunto da lista de animais é: ', conjuntoanimais)
listanimais = list(conjuntoanimais)
print('A lista do conjunto de animais é: ', listanimais)