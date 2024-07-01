"""
iterando strings com while
"""
#       012345678910111213
nome = 'vitor oliveira' # iteraveis       
#       131211109876543210

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
    
