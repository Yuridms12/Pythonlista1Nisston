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

Lista1 = [100, 25, 50, 75]
maior = max(Lista1)
menor = min(Lista1)
print(f'O maior número da lista é {maior}, e o menor número da lista é {menor}.')

#Questão 5 

