with open('meuarquivo.txt', 'r', encoding='UTF-8') as file:
    conteudo = file.read()

palavras = conteudo.split()
quantidade = len(palavras)
print(quantidade)