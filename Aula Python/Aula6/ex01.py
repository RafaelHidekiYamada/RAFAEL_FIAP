with open('meuarquivo.txt', 'w', encoding="UTF-8") as file:
    file.write('Olá Mundo\n')
    file.write('Este é um arquivo de texto\n')
    file.write('Criado por Rafael\n')

with open('meuarquivo.txt', 'r', encoding="UTF-8") as file:
    conteudo = file.read()
    print(conteudo)