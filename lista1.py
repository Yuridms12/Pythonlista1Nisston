import random

#Questão 1
n1 = int(input('Digite 1 número'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite mais 1 número'))
media = (n1 + n2 + n3) /3
print(media)

#Questão 2
o2 = int(input('Digite 1 número par ou ímpar'))
if o2 % 2 == 0:
    print(f'Esse número, {o2}, é par')
else :
    print(f'Esse número, {o2}, é ímpar')
    
#Questão 3

o3 = int(input('Digite 1 número'))
print(f'Números pares de 0 até {o3}:')
for o in range(0, o3 + 1):
    if o % 2 == 0:
        print(o)

#Questão 4

Lista1 = [15, 10, 7, 5]
maior = max(Lista1)
menor = min(Lista1)
print(f'O maior número da lista é {maior}, e o menor número da lista é {menor}.')

#Questão 5 
listanum = [7, 2, 3, 15, 12]
listapar = [jsa for jsa in listanum if jsa % 2 == 0 ]
if listapar: 
    mediapar = sum(listapar) / len(listapar)
    print(f'A média dos numeros pares é: {mediapar}')

#Questão 6 

numfat = int(input('Digite um número'))

if numfat < 0:
    print('O número tem que ser positivo!')
else:
    fatorial = 1
    for u in range(1, numfat + 1):
        fatorial *= u
        print(f'O fatorial de {numfat} é: {fatorial} ')

#Questão 7

numlimfib = int(input('Digite um número: '))
pri = 0
seg = 1
while pri <= numlimfib:
    print(pri, end=', ')
    pri, seg = seg, pri + seg
    

#Questão 8
def primo(asg):
    if asg <= 1:
        return False
    if asg == 2:
        return True
    if asg % 2 == 0:
        return False
    for i in range(3, int(asg**0.5) + 1, 2):
        if asg % i == 0:
            return False
    return True

asg = int(input('Digite um número: '))
if primo(asg):
    print(f'{asg} é um número primo')
else:
    print(f'{asg} não é um número primo')

#Questão 9

listanom = ['Alexandre', 'Barbosa', 'Gracielle', 'Alejandro', 'Yuri', 'Marcos', 'Adenor']
nomea = [jsb for jsb in listanom if jsb.startswith('A')]
print(nomea)

#Questão 10

def compu():
    return random.choice(['Pedra', 'Papel', 'Tesoura'])
def vence(usuario, computador):
    if usuario == computador:
        return 'Empate!'
    elif (usuario == 'Tesoura' and computador == 'Papel') or \
         (usuario == 'Pedra' and computador == 'Tesoura') or \
         (usuario == 'Papel' and computador == 'Pedra'):
        return 'O usuário ganhou!'
    else:
        return 'O computador ganhou!'
usuario = input('(Primeira letra em maiúsculo! ) Escolha Pedra, Papel ou Tesoura: ').strip().capitalize()
if usuario not in ['Pedra', 'Papel', 'Tesoura']:
    print('Escolha inválida!')
else:
    computador = compu()
    print(f'O computador escolheu: {computador}')
    resultado = vence(usuario, computador)
    print(resultado)
