"""Implementar  um  algoritmo  que  calcule  e  escreva  o  somatório  dos  valores  armazenados 
numa variável unidimensional A de 10 elementos numéricos a serem lidos do teclado."""
#IMPORTAR BIBLIOTECA PARA RANDOMIZAR OS NUMEROS
from random import randint

#DETERMINAR UM VETOR
vet = []

#INSERIR OS VALORES DENTRO DO VETOR
for i in range(10):
    num = randint(1,10)
    vet.append(num)

#SOMAR OS VALORES DENTRO DO VETOR
soma = sum(vet)

print(f"A soma dos valores do vetor {vet} é igual a {soma}")