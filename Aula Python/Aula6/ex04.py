conteudo = ""
with open('arquivoex03.txt', 'r', encoding="UTF-8") as file:
    conteudo = file.read()

conteudo = conteudo.replace(',', '')
conteudo = conteudo.replace('á', 'a')
conteudo.replace('~', '')
conteudo.replace('^', '')
palavras = conteudo.split()
palavra = input('Digite uma palavra: ')

if palavra in palavras:
    print(palavra)
else:
    print(f'A palavra "{palavra}" não existe')
