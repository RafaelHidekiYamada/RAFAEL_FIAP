class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    lista_pessoas = []
    def adicionar_pessoa(self):
        self.lista_pessoas.append(self)
        print(f"{self.nome} foi adicionado à lista de pessoas.")
    def mostrar_pessoas(self):
        print("Lista de pessoas:")
        for pessoa in self.lista_pessoas:
            print(f"{pessoa.nome}, {pessoa.idade} anos, {pessoa.peso} kg, {pessoa.altura} m, sexo {pessoa.sexo}.")
