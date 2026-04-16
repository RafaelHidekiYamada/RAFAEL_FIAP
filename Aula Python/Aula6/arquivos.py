# Abrir arquivo para escrita
with open('arquivo.txt','w',encoding="UTF-8") as file: # encoding serve para puxar a linguagem que tem acento
    file.write('Olá, mundo!\n')
    # Escreve no arquivo
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

# Abrir arquivo para leitura e escrita (apenas leitura é (r))
with open('arquivo.txt', 'r+', encoding="UTF-8") as file:
    conteudo = file.read()
    file.write('\nAdcionando mais conteúdo')

# Abrir arquivo para anexo
with open('arquivo.txt', 'a', encoding="UTF-8") as file:
    file.write('\nMais uma linha no final do arquivo.')

# Abre o arquivo no mode de leitura ('r')
with open('arquivo.txt', 'r') as file:
    #Lê todo o conteúdo do arquivo
    conteudo = file.read
    print(conteudo)

# Abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as file:
    # Lê a primeira linha do arquivo
    linha1 = file.readline()
    # Lê a segunda linha do arquivo
    linha2 = file.readline()
    # Lê a terceira linha do arquivo
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)