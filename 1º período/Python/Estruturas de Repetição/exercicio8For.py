'''Leia a idade de 20 pessoas e exiba a média das idades.'''
media = 0
for i in range(1,21):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    media = idade
    media = (media + idade) / 20 
print('A média de todas as idades inseridas é igual a {} anos'.format(media))