try:
    num = int(input('digite um numero: '))
    antecessor = num - 1
    sucessor = num + 1
    print(f'Analisando seu número, o antecessor de {num} é {antecessor} e o sucessor de {num} é {sucessor}')
except ValueError:
    print('Digite um número inteiro')


