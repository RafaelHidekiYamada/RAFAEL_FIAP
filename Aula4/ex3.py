def media(num):
    return sum(num)/len(num)
num = []
for e in range(5):
    numero = float(input('Digite o numero: '))
    num.append(numero)
resultado = media(num)
print(f'A media é: {resultado}')