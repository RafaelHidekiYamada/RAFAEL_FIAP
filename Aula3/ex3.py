matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
transposta = []
for i in range(2):  # número de colunas da matriz original
    linha = []
    for j in range(3):  # número de linhas da matriz original
        linha.append(matriz[j][i])
    transposta.append(linha)

for linha in transposta:
    print(linha)