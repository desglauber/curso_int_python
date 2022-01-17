list = [1, 3, 5, 7]
print('O tipo abaixo é: ', type(list))
print(list)
print('O total da lista é: ', sum(list))
print('O o maior valor da lista é: ', max(list))
print('O menor valor da lista é: ', min(list))

animal_list = ['cachorro', 'gato', 'elefante']
print('O tipo é: ', type(animal_list))
print(animal_list)
print('A posição 1 é: ', animal_list[1])
print('O o maior valor da lista de animais é: ', max(animal_list))
print('O menor valor da lista de animais é: ', min(animal_list))
print('Abaixo consta o conteúdo da lista de animais')
for x in animal_list:
    print(x)

read_animal = str(input('Digite o nome do animal: '))
if read_animal in animal_list:
    print('O animal {} está na lista.'.format(read_animal))
else:
    print('O animal {} não está na lista. O mesmo será incluído.'.format(read_animal))
    animal_list.append(read_animal)
    print('A lista de animais foi atualizada.')
    print(animal_list)

#Ordenando as listas
animal_list.sort()
list.sort()
print('As listas foram ordenadas')
print(list, animal_list)

#Desordenando as listas
animal_list.reverse()
list.reverse()
print('As listas foram desordenadas')
print(list, animal_list)

#Retirar uma posição da lista de animais
remove = int(input('Qual posição devo retirar da lista de animais? '))
animal_list.pop(remove)
print(animal_list)

#Multiplicar uma lista
mult = int(input('Digite o valor para multiplicar as listas de números e de animais: '))
animal_list *= mult
list *= mult
print(animal_list)
print(list)

#Tamanho da lista
print('O tamanho da lista de animais é: ', len(animal_list))
print('O tamanho da lista numérica é: ', len(list))

print('Fim da execução')