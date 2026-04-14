matriz = [
   # 0  1  2 | segundo numero
    [1, 2, 3],# 0
    [4, 5, 6],# 1 | primeiro numero
    [7, 8, 9] # 2
]
print(matriz[1][2]) # puxou a linha 1 e o numero na posicao 2

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# adicionando nova linha a matriz
nova_linha = [10, 11, 12]
matriz2.append(nova_linha)
#imprimindo a matriz atualizada
for linha in matriz2:
    print(linha)

# matriz inicial
matriz3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# adicionando um elemento (100) a segunda linha na primira posição
matriz3[1].insert(0, 100)
# imprimindo a matriz atualizada
for n in matriz3:
    print(n)
# matriz inicial
matriz4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# usando 'del' para a segunda linha
del matriz4[1]

# imprimindo a matriz após a remoção da segundo linha
print('Matriz após a remoção da segunda linha: ')
for z in matriz4:
    print(z)

# usando 'pop' para remover e obter o elemento na terceira coluna da primeira linha
elemento = matriz4[0].pop(2)
print(f'\nElemento removido, {elemento}')
# imprimindo a matriz após a remoção do elemento
print('\nMatriz após a remoção do elemento: ')
for j in matriz4:
    print(j)

# matriz de exemplo
matriz5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# alterar sobre cada elemento da linha
for k in matriz5:
    for elemento2 in k:
        print(elemento2, end=' ')
# imprimir uma nova linha após cada linha da matriz
    print()