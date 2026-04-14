def calcular_fatorial(n):
    resultado = 1
    if n == 0 or n == 1:
        return 1
    
    for i in range(n, 0, -1):
        resultado = resultado * i
    return resultado

numero = int(input('Digite um numero: '))
print(f'O fatorial do {numero} é {calcular_fatorial(numero)}')