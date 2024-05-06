'''Desenvolva um algoritmo que leia um número não determinado de valores e calcule e
escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a
quantidade de valores negativos e o percentual de valores negativos e positivos.'''
cont = 0
positivo = 0
negativo = 0
while cont>1:
    valor = float(input('Digite um valor inteiro qualquer: [0] para parar '))
    media = valor
    media = (media + valor) / cont
    cont += 1
    if valor == 0:
        break
    elif valor <0:
        negativo = negativo + 1
    elif valor > 0:
        positivo = positivo + 1
print('Foram entranhados {} números positivos\n{} Números negativos\nE a média entre todos os números é igual a {}'.format(positivo,negativo,media))
    
