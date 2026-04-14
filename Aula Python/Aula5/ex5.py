def verificar_palidromo(texto):
    texto = texto.lower()
    
    texto_invertido = ""

    for letra in texto:
        texto_invertido = letra + texto_invertido
    
    if texto == texto_invertido:
        return True
    else:
        return False
    
frase = input("Digite uma palavra: ")
print(verificar_palidromo(frase))