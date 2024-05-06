'''Escreva um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a
tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N =
10N.'''
valor = int(input('Digite qualquer valor inteiro entre 1 e 10: '))
cont = 0
while cont <10:
    cont += 1
    print('{} x {} = {}'.format(cont,valor,cont*valor))