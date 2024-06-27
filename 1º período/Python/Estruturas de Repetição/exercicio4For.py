'''Faça um algoritmo que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e a média de valores pares. O número que
encerrará a leitura será zero.'''
par = 0
cont = 0
media = 0
for i in range(1, 999):
    valor = int(input('Entranhe qualquer número positivo: [0] para encerrar '))
    if valor % 2 == 0:
        cont += 1
        valor = valor + 1
        media = valor
        media = (media + valor) / cont
print('Foram entranhados {} números pares\nA média de números pares foi de {}'.format(par,media))