"""Criar um vetor A com 15 elementos inteiros. Construir um vetor B de mesmo tipo e
tamanho, sendo que cada elemento do vetor B deverá ser o quadrado do respectivo elemento
de A. mostre ambos os vetores na tela"""
#DETERMINAR VETORES
vet_a = []
vet_b = []

#INSERIR 15 VALORES NO VETOR A
for i in range(0,15):
    num = float(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)

#COPIAR OS VALORES DO VETOR A NO VETOR B
for i in range(0,15):
    vet_b.append(vet_a[i]**2)

#IMPRIMIR OS VETORES
print(f"VETOR A = {vet_a}")
print(f"VETOR B = {vet_b}")