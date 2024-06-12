"""Criar em vetor A com 10 elementos inteiros. Imprima na tela. A seguir, substitua todos os
elementos ímpares por 0 e imprima novamente o vetor A na tela."""
#DETERMINAR O VETOR
vet_a = []

#INSERIR VALORES NO VETOR
for i in range(10):
    num = float(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)

#IMPRIMIR VETOR A
print(f"VETOR A = {vet_a}")

#SUBSTITUIR VALORES DO VETOR A
for i in range(10):
    vet_a[i]=vet_a[i]*0

#IMPRIMIR VETOR A COM VALORES SUBSTITUIDOS
print(f"VETOR A = {vet_a}")


