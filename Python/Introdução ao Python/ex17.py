'''Faça um programa para calcular e apresentar o volume de uma lata de óleo, utilizando a fórmula volume=3.14159*raio*raio*altura. Identifique na formula os valores de entrada de dados
e leia-os via teclado'''
raio=float(input('Informe o raio da lata de óleo em centimetros: ')) # Valor de entrada
altura=float(input('Informe a altura da lata de óleo em centimetros: ')) # Valor de entrada
volume=(3.14159*raio*raio)*altura # Valor de saída
print('O volume da lata de óleo é correspondente à {:.2f}cm³'.format(volume)) # Valor de saída