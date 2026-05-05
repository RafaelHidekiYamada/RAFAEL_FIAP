class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    def descrever(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, Altura: {self.altura} m, Sexo: {self.sexo}.")