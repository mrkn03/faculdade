"""Fazer um programa para receber 10 números inteiros e criar um segundo vetor só com os
valores do primeiro que são divisíveis por 5. Mostre ambos os vetores na tela."""
#DETERMINAR OS VETORES
vet_a = []
vet_b = []

#INSERIR VALORES NO VETOR A
for i in range(10):
    num = float(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)

#INSERIR VALORES DO VETOR A QUE SAO DIVISIVEIS POR 5
for i in vet_a:
    if i % 5 ==0:
        vet_b.append(i)

#IMPRIMIR VETORES
print(f"VETOR A = {vet_a}")
print(f"VETOR B = {vet_b}")