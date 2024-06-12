"""Criar dois vetores A e B cada um com 10 elementos inteiros. Construir um vetor C, onde
cada elemento de C é a multiplicação dos respectivos elementos em A e B, ou seja: C[i] = A[i] *
B[i]. Após isso, some todos os elementos de C.
Mostre todos os vetores na tela, bem como a soma calculada por último."""
#DETERMINAR VETORES
vet_a = []
vet_b = []
vet_c = []

#INSERIR VALORES NO VETOR A
for i in range(10):
    num = float(input(f"Digite o {i+1}º valor"))
    vet_a.append(num)

#INSERIR VALORES NO VETOR B
for i in range(10):
    num = float(input(f"Digite o {i+1}º valor"))
    vet_b.append(num)

#MULTIPLICAR VETOR A E VETOR B
for i in range(10):
    vet_c.append(vet_a[i] * vet_b[i])

#IMPRIMIR VETORES
print(f"VETOR A = {vet_a}")
print(f"VETOR B = {vet_b}")
print(f"VETOR C = {vet_c}")