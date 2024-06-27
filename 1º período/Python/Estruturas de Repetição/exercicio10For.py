'''Faça um algoritmo que leia 2 valores inteiros e positivos: X e Y. O algoritmo deve
calcular e escrever a função potência XY'''
for i in range(1,999):
    valor1 = int(input('Digite o primeiro valor: [0] para encerrar '))
    valor2 = int(input('Digite o segundo valor: [0] para encerrar'))
    if valor1 or valor2 ==0:
        break
    else:
        potencia = valor1 ** valor2
print('O resultado da potencia entre os valores {} e {} é igual a {}'.format(valor1,valor2,potencia))