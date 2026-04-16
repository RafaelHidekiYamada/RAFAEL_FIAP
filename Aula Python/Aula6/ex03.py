arquivo = ""
meuarquivo = ""

with open('arquivo.txt', 'r', encoding="UTF-8") as file:
    arquivo = file.read()

with open('meuarquivo.txt', 'r', encoding="UTF-8") as file:
    meuarquivo = file.read()

with open('arquivoex03.txt', 'a', encoding="UTF-8") as file:
    file.write(arquivo)
    file.write(meuarquivo)