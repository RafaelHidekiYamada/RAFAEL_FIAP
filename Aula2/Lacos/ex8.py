print('Exercicio 8')
import random
tentativas = 2
num = 5
num = random.randint(1,10) # vai gerar um numero aleatorio entre 1 - 10
user_num = int(input('Digite um numero entre 1 - 10: ')) # numero que o usuario digitar
while user_num != num and tentativas > 0: # enquanto o numero do usario for diferente do num e as tentativas forem maior que 0
    print(f'Tentativas restantes {tentativas}')
    user_num = int(input('Digite um numero entre 1 - 10: '))
    tentativas -= 1
if user_num != num and tentativas == 0: # se o numero do usuario for diferente do num e as tentativas forem igual a 0 
    print('Parabens, vc é definitivamente um USUARIO')
    print(f'O numero era {num}')
else: # se não, execute isso
    print('Parabens, vc foi promovido a PROGRAMADOR')