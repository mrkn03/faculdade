'''Escreva um algoritmo que leia um valor inicial (A – A tem que ser inteiro e positivo),
calcule a soma dos números de 1 até A e mostre o seu resultado.'''
valor = int(input('Digite um valor inteiro qualquer: '))
soma = 0
for i in range(1,valor):
    soma = valor
    soma = soma + (1 * valor)
print('A soma de 1 até chegar a {} é igual a {}'.format(valor,soma))
