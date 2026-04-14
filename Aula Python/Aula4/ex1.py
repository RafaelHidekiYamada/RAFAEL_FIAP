def adicao(num, num2):
    return num+num2

def subtracao(num, num2):
    return num-num2

def mutiplicacao(num, num2):
    return num*num2

def divisao(num, num2):
    return num/num2

num = float(input('Digite o numero: '))
num2 = float(input('Digite o outro numero: '))
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
operacao = int(input('Digite o Numero de acordo com a operação desejada: '))

while True:
    match operacao:
        case 1:
            soma = adicao(num, num2)
            print(f'A soma é: {soma}')
            break
        case 2:
            sub = subtracao(num, num2)
            print(f'A subtração é: {sub}')
            break
        case 3:
            multi = mutiplicacao(num, num2)
            print(f'A multiplacação é: {multi}')
            break
        case 4:
            div = divisao(num, num2)
            print(f'A divisão é: {div}')
            break
        case _:
            print('Opção Invalida!')
            operacao = int(input('Digite o numero de acordo com a operação desejada: '))