'''Uma empresa vende produtos para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
8%). Faça um programa em que o usuário entre com o nome, o valor e a sigla do estado
destino de dez produtos e o programa escreve na tela o preço final de cada produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for
válido, mostrar uma mensagem de erro.'''
cont = 1
while True:
    nome = str(input('Digite seu nome:'))
    valor = float(input('Digite o valor do produto: R$'))
    estado = str(input('Digite a sigla do seu estado: ')).upper()
    cont += 1
    if cont < 10:
        if estado == 'MG':
            valor = valor + (valor* 0.07)
            print('Senhor {} o preço do produto acrescido com os impostos de sua região é igual a R${}'.format(nome,valor))
        elif estado == 'SP':
            valor = valor + (valor * 0.12)
            print('Senhor {} o preço do produto acrescido com os impostos de sua região é igual a R${}'.format(nome,valor))
        elif estado == 'RJ':
            valor = valor + (valor * 0.15)
            print('Senhor {} o preço do produto acrescido com os impostos de sua região é igual a R${}'.format(nome,valor))
        elif estado == 'MS':
            valor = valor + (valor* 0.08)
            print('Senhor {} o preço do produto acrescido com os impostos de sua região é igual a R${}'.format(nome,valor))
    else:
        break