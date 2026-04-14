print('Exercicio 1\n')
print('1. Ver Perfil\n')
print('2. Editar Perfil\n')
print('3 . Sair\n')
menu = int(input('Digite um numero: '))
while True: # o laço estara ativo ate ser interrompido
    match menu:
        case 1:
            print('Ver Perfil Escolhido\n')
            break # interrompe o laço
        case 2:
            print('Editar Perfil Escolhido\n')
            break
        case 3:
            print('Saindoooo...\n')
            break
        case _:
            print('Opção Invalida\n')
            menu = int(input('Digite um numero novamente: '))

print('Exercicio 2\n')
dia = int(input('Digite o dia da semana em numero: '))
while True:
    match dia:
        case 1:
            print('Domingo\n')
            break
        case 2:
            print('Segunda-Feira\n')
            break
        case 3:
            print('Terca-Feira\n')
            break
        case 4:
            print('Quarta-Feira\n')
            break
        case 5:
            print('Quinta-feira\n')
            break
        case 6:
            print('Sexta-Feira\n')
            break
        case 7:
            print('Sabado\n')
            break
        case _:
            print('Opção Invalida!')
            dia = int(input('Digite o dia da semana em numero novamente: '))

print('Exercicio 3\n')
numero = int(input('Digite um numero de acordo com o mes: '))
while True:
    match numero:
        case 12 | 1 | 2:
            print('Verão')
            break
        case 3 | 4 | 5:
            print('Outono')
            break
        case 6 | 7 | 8:
            print('Inverno')
            break
        case 9 | 10 | 11:
            print('Primavera')
            break
        case _:
            print('Opção Invalida!')
            numero = int(input('Numero do mes invalido! Digite novamente: '))

print('Exercicio 4\n')
idade = int(input('Digite sua idade: '))
match idade:
    case idade if idade > 0 < 13:
        print('Categoria KIDS')
    case idade if idade > 12 < 18:
        print('Categoria Jovem')
    case idade if idade > 18:
        print('Adulto')

print('Exercicio 5')
nota = int(input('Digita uma nota de 0 a 10: '))
match nota:
    case nota if nota > 8 < 11:
        print('Resultado Execelente')
    case nota if nota > 6 < 9:
        print('Resultado Bom')
    case nota if nota > 4 < 7:
        print('Resultado Regular')
    case nota if nota < 5:
        print('Resultado Reprovado')