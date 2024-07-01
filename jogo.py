placar = 'CORRETAAAAAA'
placar2 = 'BURROSSSSS'
intro = input('!!VAMOS PARA A PRIMEIRA PERGUNTA!!')

pergunta1 = input('1- O que é Afinidade Química? ')

print('                             ')
print('A) Capacidade que uma substância tem de reagir com a outra.')
print('B) Quando a substância não tem de reagir com a outra.')
print('C) É a propriedade eletrônica pela qual espécies químicas iguais são capazes de formar compostos químicos.')
print('D) É um tipo de fusão entre Metais Alcalinos e Gases Nobres')

print('                ')
resposta1g1 = input('Resposta do grupo 1: ')
print(' ')
resposta1g2 = input('Resposta do grupo 2: ')
print(' ')
if resposta1g1 == "A":
    print(placar)
else:
    print(placar2)
if resposta1g2 == "A":
    print(placar)
else:
    print(placar2)
print('     ')
cont1 = input('Segunda pergunta!')
print('  ')
pergunta2 = input('2- Um átomo que tem uma camada com 5 elétrons e uma com 3 elétron tem a tendência de buscar mais um elétron e isso faz com que aconteca estabilização ao átomo.')

resposta2g1 = input('Grupo 1: verdadeiro ou falso? ')
print(' ')
resposta2g2 = input('Grupo 2: verdadeiro ou falso? ')
if resposta2g1 == 'FALSO':
    print(placar)
else:
    print(placar2)
if resposta2g2 == 'FALSO':
    print(placar)
else:
    print(placar2)
print(' ')
cont3 = input('TERCEIRA QUESTÃO!!')
pergunta3 = input('3- Com quais substâncias não ocorrem afinidade química? ')
print('  ')
print('A) Sódio e Água.')
print('B) Água e Potássio.')
print('C) Querosene e Sódio.')
print('D) Potássio e Enxofre.')
resposta3g1 = input('Grupo 1: qual a alternativa? ')
print(' ')
resposta3g2 = input('Grupo 2: qual alternativa? ')
print('  ')
if resposta3g1 == 'C':
    print(placar)
else:
    print(placar2)
if resposta3g2 == 'C':
    print(placar)
else:
    print(placar2)
print('  ')
cont4 = input('VAMO DALE PRA QUARTA QUESTÃO???')
print(' ')
pergunta4 = input('4- O que acontece quando não há uma afinidade qímica entre as substâncias?')
print('  ')
print('A) Nada.')
print('B) Elas reagem uma à outra.')
print('C) Elas mudam sua camada de valência.')
print('D) Elas viram um Cátion postivo.')
resposta4g1 = input('Grupo 1: qual alternativa? ')
print('  ')
resposta4g2 = input('Grupo 2: qual alternativa?')
print(' ')
if resposta4g1 == 'A':
    print(placar)
else:
    print(placar2)
print(' ')
if resposta4g2 == 'A':
    print(placar)
else:
    print(placar2)
print(' ')
cont5 = input('VAMOS PARA A ÚLTIMA PERGUNTA!!')
pergunta5 = input('5- A velocidade com que as reações se processam varia muito, e existem alguns fatores que interferem não só nessa velocidade, mas até mesmo na ocorrência dessas reações. Eles são basicamente quatro: contato entre os reagentes, afinidade química, colisões favoráveis e energia de ativação.')
print(' ')
resposta5g1 = input('Grupo 1: verdadeiro ou falso?')
print(' ')
resposta5g2 = input('Grupo 2: verdadeiro ou falso?')
if resposta5g1 == 'VERDADEIRA':
    print(placar)
else:
    print(placar2)
if resposta5g2 == 'VERDADEIRA':
    print(placar)
else:
    print(placar2)
print('--------------------------------------------------------------------------------------------------------------')
print(' ')
if placar in resposta1g1:
    print('grupo 1 acertou a primeira')
else:
    print('Grupo 1 errou a primeira')

if placar in resposta1g2:
    print('grupo 2 acertou a primeira')
else:
    print('Grupo 2 errou a primeira')

if placar in resposta2g1:
    print('grupo 1 acertou a primeira')
else:
    print('Grupo 1 errou a primeira')

if placar in resposta2g2:
    print('grupo 1 acertou a primeira')
else:
    print('Grupo 1 errou a primeira')



if placar in resposta3g1:
    print('grupo 1 acertou a primeira')
else:
    print('Grupo 1 errou a primeira')

if placar in resposta3g2:
    print('grupo 1 acertou a primeira')
else:
    print('Grupo 1 errou a primeira')

if placar in resposta4g1:
    print('grupo 1 acertou a quarta')
else:
    print('Grupo 1 errou a quarta')

if placar in resposta4g2:
    print('grupo 2 acertou a quarta')
else:
    print('Grupo 2 errou a quarta ')

if placar in resposta5g1:
    print('grupo 1 acertou a quinta')
else:
    print('Grupo 1 errou a quinta')

if placar in resposta5g2:
    print('grupo 2 acertou a quinta')
else:
    print('Grupo 2 errou a quinta')