def poderada():
    soma_valores = 0
    soma_pesos = 0
    quantidade = 3
    
    for i in range(quantidade):
        nota = float(input(f'Digite a {i+1}° nota: '))
        pesos = float(input(f'Digite a {i+1}° peso: '))
        soma_valores += nota * pesos
        soma_pesos += pesos

    media_ponderada = soma_valores / soma_pesos
    print(f'A media ponderada é: {media_ponderada:2f}')

poderada()
