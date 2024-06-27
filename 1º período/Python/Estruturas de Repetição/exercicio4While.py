'''Faça um algoritmo que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e a média de valores pares. O número que
encerrará a leitura será zero.'''
cont = 0
par = 0
media = 0
while cont > 1:
    valor = int(input('Entranhe qualquer valor inteiro: [0] para encerrar '))
    if valor % 2 ==0:
        par += 1
        cont += 1
        media = valor
        media = (media + valor) / cont
print('Foram entranhados {} valores positivos\nE a média dos números pares é igual a {}'.format(par,media))