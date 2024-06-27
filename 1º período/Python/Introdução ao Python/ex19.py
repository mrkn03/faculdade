'''Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar ao final do programa o seu nome, o salário fixo e salário no final do mês.'''

nome=str(input('Informe o nome do vendedor: '))
salario_fixo=float(input('Informe o salário fixo do vendedor: R$'))
vendas=float(input('Informe o valor de vendas efetuadas no mês: R$'))
salario_final=salario_fixo+(vendas*15/100)
print('O vendedor {} recebe o salário fixo de R${} e fez o total de R${} em vendas, com sua comissão mensal ele receberá R${} neste mês.'.format(nome,salario_fixo,vendas,salario_final))
