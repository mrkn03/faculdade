'''Escreva um algoritmo que leia um valor inicial (A – A tem que ser inteiro e positivo),
calcule a soma dos números de 1 até A e mostre o seu resultado.'''
valor = int(input('Digite um valor inteiro qualquer: '))
cont = 0
soma = 0
while cont < valor:
    soma = valor
    soma = soma + (1 * valor)
print('A soma de 1 até chegar no valor {} é igual a {}'.format(valor,soma))
