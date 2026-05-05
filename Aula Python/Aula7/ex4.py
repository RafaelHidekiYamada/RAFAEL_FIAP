class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            print(f"{self.nome} é mais velho(a) que {outra_pessoa.nome}.")
        elif self.idade < outra_pessoa.idade:
            print(f"{self.nome} é mais novo(a) que {outra_pessoa.nome}.")
        else:
            print(f"{self.nome} e {outra_pessoa.nome} têm a mesma idade.")