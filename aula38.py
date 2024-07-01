"""cauculadora com while"""
while True:
    num1 = input('digite o primeiro numero: ')
    num2 = input('digite o segundo numero: ')
    operador = input('digite um dos operadores (+-*/): ')
    
    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True 

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('voce digitou um ou ambos numeros invalidos')
        continue 
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('operador invalido.')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    if operador == '+':
        print(f'seu resultado é: {num1_float + num2_float}')
    elif operador == '-':
        print(f'seu resultado é: {num1_float - num2_float}')
    elif operador == '*':
        print(f'seu resultado é; {num1_float * num2_float}')
    elif operador == '/':
        print(f'seu resultado é: {num1_float / num2_float}')
    else:
        print('como voce chegou a esse de ponto?')

    sair = input('voce quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


   