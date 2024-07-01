try:  
    nota1 = float(input('Digite nota 1:'))
    nota2 = float(input('Digite nota 2:'))
    media = nota1 + nota2 / 2
    print(media)
except ValueError:
    pass