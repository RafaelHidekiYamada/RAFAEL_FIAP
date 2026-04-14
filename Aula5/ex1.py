def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
        lista_fibonacci.append(a)
        soma = sum(lista_fibonacci)
    print(f'\nA soma dos termos da sequência de Fibonacci é: {soma}')
lista_fibonacci = []
numero = int(input('Digite o número de termos da sequência de Fibonacci: '))
fibonacci(numero)