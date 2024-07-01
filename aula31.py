"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('digite um numero inteiro: ')

# try:
#     entrada_int = int(entrada)
# except ValueError:
#    print('isso nao é um numero inteiro válido')
#    exit()

# if entrada_int % 2 == 0:
#    print('Este número é par')
# elif entrada_int % 2 >= 1:
#    print('Este número é ímpar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# try:
#     horas = int(input('Que horas são?(respeitando o formato "24 horas") '))
#     if horas >= 0 and horas <= 11:
#         print(f'Bom dia, agora é: {horas} horas')
#     elif horas >= 12 and horas <= 17:
#         print(f'Boa tarde, agora são: {horas} horas ')
#     elif horas >= 18 and horas <= 23:
#         print(f'Boa noite, agora são: {horas} horas')
#     else:
#         print('desconheço esta hora')

# except (ValueError or TypeError):
#     print('Digite numeros inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    nome = str(input('Digite seu nome: '))
    len = len(nome)
    lenstr = str(len)

    if lenstr <= 4:
        print(f'{nome}, seu nome é curto.')
    elif lenstr == 5 or lenstr == 6:
        print(f'{nome}, seu nome é normal.')
    elif lenstr >= 7:
        print(f'{nome}, seu nome é muito grande.')

except TypeError:
    print('Digite um nome válido')