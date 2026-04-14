def maior(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

numero2 = []
contador = 3
while contador > 0:
    numeros = int(input('Digite um numero: '))
    numero2.append(numeros)
    contador -= 1
resultado = maior(numero2[0], numero2[1], numero2[2])
print(f'O maior numero é {resultado}')