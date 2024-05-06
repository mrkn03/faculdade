'''Desenvolva um algoritmo que efetue a soma de todos os números ímpares que são
múltiplos de três e que se encontram no conjunto dos números de 1 até 500.'''
cont = 0
soma = 0
while cont < 10:
    if cont % 2 != 0:
        if cont % 3 ==0:
            soma = cont
            soma = soma + cont
print('A soma de todos os números ímpares e divisíveis por 3 é igual a {}'.format(soma))