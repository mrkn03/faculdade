'''Escreva um algoritmo que leia 20 números do usuário e exiba quantos números são
maiores do que 10.'''
maior10 = 0
for i in range(1,21):
    numero = int(input('Digite um número inteiro qualquer: '))
    if numero > 10:
        maior10 = maior10 + 1
print('Foram encontrados {} números maiores que 10.'.format(maior10))