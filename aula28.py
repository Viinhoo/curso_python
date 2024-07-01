"""
introduçao ao try/except
tru -> tentar executar o codigo
except -> ocorreu algum erro aao tentar  executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')