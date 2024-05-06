'''Leia a idade de 20 pessoas e exiba a média das idades.'''
cont = 0
while cont <20:
    cont +=1
    idade = int(input('Digite a idade da {}ª pessoa: '.format(cont)))
    media = idade
    media = (media + idade) / 20
print('A média de todas as idades inseridas é igual a {} anos'.format(media))
