vogais = ['a','e','i','o','u']
frase = input('Digite uma frase: ')

def contar_vogal(frase):
    contador = 0
    frase = frase.lower()
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

total = contar_vogal(frase)

print(f'O numero de vogais é {total}')