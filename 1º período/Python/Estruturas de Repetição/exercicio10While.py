'''Faça um algoritmo que leia 2 valores inteiros e positivos: X e Y. O algoritmo deve
calcular e escrever a função potência XY'''
cont = 1
while cont > 1:
    cont +=1
    valor1 = int(input('Digite o primeiro valor: [0] para parar '))
    valor2 = int(input('Digite o segundo valor: [0] para parar '))
    if valor1 or valor2 == 0:
        break
    else:
        potencia = valor1 ** valor2
print('O resultado da potenciação entre os valores {} e {} é igual a {}'.format(valor1,valor2,potencia))