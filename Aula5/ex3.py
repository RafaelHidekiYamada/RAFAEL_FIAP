def somas_digitos(numero):
    texto_do_numero = str(numero)
    soma = 0
    for digito in texto_do_numero:
        soma = soma + int(digito)
    return soma
n = int(input('Digite um numero: '))
resultado = somas_digitos(n)
print(resultado)