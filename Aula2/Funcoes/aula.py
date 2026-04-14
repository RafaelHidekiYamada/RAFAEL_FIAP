numeros = [1, 2, 3] # lista

numeros.append(4) # para adicionar um ITEM na lista

numeros2 = [5,6,7] # outra lista

print(numeros)

numeros.extend(numeros2) # para adicionar uma lista em outra

print(numeros)

numeros.insert(6,10)

numeros.insert(4,10)
# para trocar um item por outro, o numero "4" representa a posição do item na lista.
# o numero 10 é o item que sera colocado no lugar da posição indicada

print(numeros)

numeros.remove(10) # remove a primeira ocorrencia do item na lista

print(numeros)

print(numeros.pop(2)) # mostra o numero indicado pelo indice e o retira da lista / indice = posição do numero
print(numeros)

print(numeros2)
numeros2.clear() # Remove todos os elementos da lista
print(numeros2)

index = numeros.index(10) # retorna o numero que foi retirado da lista
print(index)

vezes = numeros.count(5) # mostra a quantidade de itens do elemento indicado
print(vezes)

numeros.sort() # ordena os elementos da lista em ordem crescente
print(numeros)

numeros.reverse() # ordena os elementos da lista em ordem decrescente
print(numeros)

numeros3 = numeros.copy() # faz uma copia rasa da lista
print(numeros3)