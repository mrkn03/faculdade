'''Desenvolva um algoritmo que leia a altura de 15 pessoas. Este programa deverá
calcular e mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo;
c. A média da altura do grupo'''
maior  = 0
menor = 999
media = 0
for i in range(1,5):
    altura = float(input('Digite a altura da {}ª pessoa em cm: ').format(i))
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
    media = altura
    media = (media + altura) / 15
print('Menor altura = {}cm\nMaior altura = {}cm\nMédia do grupo = {}cm'.format(menor, maior, media))
