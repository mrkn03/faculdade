'''Você irá fazer uma viagem internacional e precisa levar seu dinheiro em dólares. Elabore um algoritmo para calcular e apresentar o valor da conversão de real (R$) para dólar US$).
O algoritmo deverá solicitar o valor da cotação do dólar e quantos Rais (R$) você tem para converter em dólar. Ao final mostre a quantidade de dólares que você irá levar para a 
viagem.'''

cotacao=float(input('Informe a cotação do dolar hoje: R$'))
reais=float(input('Informe a quantidade de real que deseja converter: R$'))
dolar=reais/cotacao
print('Com R${} você conseguirá comprar US${:.2f}'.format(reais,dolar))
