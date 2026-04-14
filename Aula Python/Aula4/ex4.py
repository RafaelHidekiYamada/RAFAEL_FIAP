vogais = ['a','e','i','o','u']
frase = input('Digite uma frase: ')

def contar_vogal(frase):
    contador = 0
    palavra = palavra.lower() # faz com que as letras ficam minusculas
    for letra in frase:
        if letra in vogais: # puxou letra por letra de acordo com o indice
            contador += 1
    return contador

total = contar_vogal(frase)

print(f'O numero de vogais é {total}')