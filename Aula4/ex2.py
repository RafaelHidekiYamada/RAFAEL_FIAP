def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input('Digite um numero para ser testado: '))

if primo(num) == True:
    print('O numero é primo')
else:
    print('O numero não é primo')