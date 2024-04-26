'''Muitos paises estao passando a usar o sistema métrico. Preparar um algoritmo para executar a conversao de celsius para fahrenheit.
A formula de conversao é: F= (9*C+160)/5, sendo F a temperatura em fahrenheit e C a temperatura em celsius'''
celsiu=float(input('Informe a temperatura em Celsius:   '))
fahrenheit=float(input('Informe a temperatura em Fahrenheit:    '))
conversao=(9*celsiu+160)/5
print('A conversao de {}°F para Celsius é igual a {}°C.'.format(fahrenheit,conversao))