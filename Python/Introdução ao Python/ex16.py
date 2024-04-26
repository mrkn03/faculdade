'''Leia 2 valores para as variaveis A e B, efetuar a troca dos valores de forma que a variavel A passe a possuir o valor da variavel B, e que a variavel B passe a possuir o valor
da variavel A. Apresentar os valores trocados pelas variaveis.'''
a=int(input('Digite um valor qualquer: '))
b=int(input('Digite outro valor qualquer: '))
print('O valor de A é igual a {} e o valor de B é igual a {}.'.format(a,b))
a,b=b,a
print('Os valores de A e B alterados são respectivamentes {} e {}'.format(a,b))