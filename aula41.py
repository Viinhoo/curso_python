# texto = 'python'

# i = 0 
# tamanhos = len(texto)

# while i < tamanhos:
#     print(texto[i], i)

#     i += 1

espaco = '---------------------------------------------------------------------------------------'

"""EXEMPLO DE USO DO WHILE
"""

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print('aquele laço acima pode ter repeticoes infinitas')

espaco = '---------------------------------------------------------------------------------'

texto = 'python'

novo_texto = ''
for letra in texto: # TRADUCAO: para cada letra em iteravel(texto) \\
    novo_texto += f'*{letra}'
    print(letra) # exiba a letra na tela
print(novo_texto)
