# Abrir arquivo para escrita
with open('arquivo.txt','w',encoding="UTF-8") as file: # encoding serve para puxar a linguagem que tem acento
    file.write('Olá, mundo!\n')
    # Escreve no arquivo
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

# Abrir arquivo para leitura e escrita (apenas leitura é (r))
with open('arquivo.txt', 'r+') as file:
    conteudo = file.read()
    file.write('\nAdcionando mais conteúdo')

# Abrir arquivo para anexo
with open('arquivo.txt', 'a') as file:
    file.write('\nMais uma linha no final do arquivo.')