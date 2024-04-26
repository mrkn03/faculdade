'''Faça um programa para ler 2 numeros inteiros, e apresente o quociente e o resto da divisao entre eles'''
num1=int(input('Digite um valor qualquer: '))
num2=int(input('Digite o valor que deseja ser dividido: '))
quociente=num1//num2
resto=num1%num2
print('O quociente e o resto da divisão entre {} e {} sao respectivamentes {} e {}'.format(num1,num2,quociente,resto))