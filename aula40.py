frase = 'aaaooo'

i = 0
apareceuv = 0
letraav = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    apareceuv_atual = frase.count(letra_atual)

    if apareceuv < apareceuv_atual:
        apareceuv = apareceuv_atual
        letraav = letra_atual

    i += 1

print(f'a letra que apareceu mais vezes foi {letraav} com "{apareceuv}"x ')
    
    