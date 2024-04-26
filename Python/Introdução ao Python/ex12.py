'''Escreva um algorítmo para determinar o consumo médio de um automóvel sendo que será fornecida via teclado a distancia total percorrida pelo automóvel e o total de combustível 
gasto'''
distancia=float(input('Digite o total de km percorridos '))
combustivel=float(input('Digite o total de combustivel consumido em litros: '))
media=distancia/combustivel
print('O consumo médio deste automóvel foi de {}L/km.'.format(media))
