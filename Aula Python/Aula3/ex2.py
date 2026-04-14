matriz = [
    [1, 2],
    [4, 5]
]
matriz2 = []
escalar = 10
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(matriz[i][j] * escalar)
    matriz2.append(linha)
for linha in matriz2:
    print(linha)