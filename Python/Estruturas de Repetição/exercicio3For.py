'''Desenvolva um algoritmo que leia um número não determinado de valores e calcule e
escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a
quantidade de valores negativos e o percentual de valores negativos e positivos.'''
media = 0
positivo = 0
negativo = 0
total = 0
for i in range(1,999):
    valor = float(input('Digite um valor inteiro qualquer: [0] para parar '))
    media = valor
    total = total + 1
    media = (media + valor) / total
    if valor >= 1:
        positivo += 1
    if valor < 0:
        negativo += 1
    if valor == 0:
        break
print('Foram entranhados {} números positivos\n{} números negativos\nE a média de todos os valores é igual a {}'.format(positivo,negativo,media))