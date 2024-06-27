'''Escreva um algoritmo que leia um valor inicial (A – A tem que ser inteiro, maior ou igual
a zero), calcule A! e mostre o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120'''
valor = int(input('Digite um valor inteiro qualquer: '))
for i in range(valor,1,-1):
    print('{}! = {} - {}')