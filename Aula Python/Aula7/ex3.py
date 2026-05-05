class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos.")

    def descrever(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, Altura: {self.altura} m, Sexo: {self.sexo}.")