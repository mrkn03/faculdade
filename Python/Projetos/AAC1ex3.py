'''Faça um programa que leia vários números inteiros positivos e informe o maior e
o menor número. A entrada de dados pára quando o usuário digitar ZERO.'''
numero = int(input('Digite um número inteiro qualquer: [0] para parar '))
maior = 0
menor = 999
cont = 0
while cont >= 0:
    numero = int(input('Digite um número inteiro qualquer: [0] para parar '))
    cont += 1
    if numero == 0:
        break
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
print('O maior número entre os {} números escolhidos, o maior número foi {} e o menor número foi {}'.format(cont,maior,menor))