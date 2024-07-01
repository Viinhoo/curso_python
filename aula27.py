nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
    
if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('seu nome contem espaço')
    else:
        print('seu nome nao contem espaço')
    print(f'seu nome tem: {len(nome)}')
    print(f'a primeira letra do seu nome é: {nome[:1:1]}')
    print(f'a ultima letra do se nome é: {nome[4::1]}')
else:
    print("descilpe voce deixou espaços vazios")



# print(f'seu nome é: {nome}')
#     print(f'seu nome invertido é: {nome[::-1]}')
#     print('seu nome contém espaços')
