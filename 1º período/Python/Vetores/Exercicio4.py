"""Escreva um algoritmo que leia um vetor de 10 elementos inteiros. Encontre e mostre o maior 
elemento e sua posição no vetor."""
#DETERMINAR O VETOR 
vet = []

#PERGUNTAR AO USUÁRIO QUANTOS NÚMEROS VAO SER INSERIDOS NO VETOR
n = int(input("Quantos números deseja digitar? "))

#INSERIR OS NÚMEROS NO VETOR
for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    vet.append(num)

#DETERMINAR O MAIOR ELEMENTO DO VETOR
max = max (vet)

#DETERMINAR A POSIÇÃO DO MAIOR ELEMENTO DO VETOR
posicao = vet.index(max)

#IMPRIMIR O MAIOR VALOR E SUA POSIÇÃO
print(f"MAIOR VALOR DO VETOR = {max}")
print(f"POSIÇÃO DO MAIOR VALOR DO VETOR = {posicao}")