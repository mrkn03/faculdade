'''Escreva um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a
tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N =
10N.'''
valor = int(input('Digite um valor entre 1 e 10: '))
for i in range(1,11):
    print('{} x {} = {}'.format(i,valor,i*valor))