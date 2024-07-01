"""
repetiçoes
while (enquanto)
executa uma açao enquanto uma condiçao fot true
loop infinito -> quando um codigo nao tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')