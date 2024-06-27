'''Construir um algoritmo para ler 3 valores reais, calcular e imprimir a média desses valores.'''

num1=float(input('Digite o primeiro valor: '))
num2=float(input('Digite o segundo valor: '))
num3=float(input('Digite o terceiro valor: '))
media = (num1+num2+num3) / 3
print('A média entre os valores {}, {} e {} é igual a {:.2f}'.format(num1, num2, num3, media))
