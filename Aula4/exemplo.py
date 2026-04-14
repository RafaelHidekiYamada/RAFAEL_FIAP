w1 = float(input('Valor de W1: '))
w2 = float(input('Valor de W2: '))
x1 = float(input('Valor de X1: '))
x2 = float(input('Valor de X2: '))
b = float(input('Valor de B: '))
y = float(input('Valor de y: '))
n = float(input('Valor de N: '))
z = w1*x1+w2*x2+b
if z >= 0:
    z = 1
else:
    z = 0

erro = y - z

att_b = b + n*erro

print(att_b)
print(erro)