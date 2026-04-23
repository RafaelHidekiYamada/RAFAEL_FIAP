# Ordenador de Linhas

conteudo = []
with open('arquivoex03.txt', 'r', encoding="UTF-8") as file:
    while True:
        cont = file.readline()
        if cont == "":
            break
        else:
            conteudo.append(cont)


conteudo.sort()

with open('arquivoex05.txt', 'w', encoding="UTF-8") as file:
    for line in conteudo:
        file.write(line)