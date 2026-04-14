pi = 3.14
raio = float(input('digite o raio a ser calculado: ')) # float transformou a variavel em float
area = pi * raio**2

print(f'Area do circulo com o {raio} apresentado é: {area}')

fahrenheit = float(input('digite a temperatura a ser convertida: '))
Cel = (fahrenheit - 32) * 5/9 
print(f'Convertento a temperatura {fahrenheit}℉ para ℃, resulta em {Cel}℃')

livro = 25
caneta = 5
gasto = (livro * 3 ) + (caneta * 2)
print(f'O valor total gasto é de: {gasto}')

distancia = 150
velocidade = 60
tempo = distancia/velocidade
horas = int(tempo) # transformou a variavel em inteiro
minutos = int((tempo - horas) * 60)
print(f'O tempo percorrido foi de {horas} horas e {minutos} minutos')