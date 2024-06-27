'''Faça um algoritmo que peça ao usuário um valor para dia, um valor para mês e
um valor para ano. O programa deve verificar se essa data é válida. O dia digitado deve
ser válido, de acordo com o mês digitado. Você deve também verificar se o ano é
bissexto.'''
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: ex[1,2,...,12]'))
ano = int(input('Digite o ano: '))
while True:
    if ano % 100 != 0 and ano % 4 == 0:
        if mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 29 and mes == 2 or dia == 31:
                print('Data - {}/{}/{} é um ano bissexto'.format(dia,mes,ano))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia == 31:
            print('Data - {}/{}/{} não é um ano bissexto'.format(dia,mes,ano))
        else:
            print('O dia inserido é inválido')
    else:
        break
    