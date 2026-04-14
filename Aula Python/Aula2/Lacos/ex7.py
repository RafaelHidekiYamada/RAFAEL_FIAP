print('Exercicio 7')
numero = int(input('Digite um numero par: '))

while numero % 2 != 0:  # while - enquanto | % - resto da divisao | ! - diferente \ enquanto o numero/2 for diferente de 0
    numero = int(input('Tente novamente, digite um numero par: \n'))
else: # Quando o while termina, ele executa o else
    print(f'O numero escolhido foi: {numero}\n')