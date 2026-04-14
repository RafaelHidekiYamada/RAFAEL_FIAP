matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz3 = [] # Essa lista vai guardar o resultado da soma das matrizes
for i in range(3): # i representa o índice da linha( 0 , 1 , 2)
    linha = [] # Para cada linha, você cria uma lista vazia que vai guardar os resultados.
    for j in range(3): # j representa o índice da coluna (0 , 1 , 2)
        linha.append(matriz[i][j] + matriz2[i][j])
        # matriz[i][j] → pega um número da primeira matriz
        # matriz2[i][j] → pega o número correspondente da segunda
        # soma os dois
        # adiciona na lista linha
    matriz3.append(linha)
for linha in matriz3:
    print(linha)