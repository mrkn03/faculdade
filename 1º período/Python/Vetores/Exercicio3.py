"""Ler dois vetores A e B com seis elementos. Construir um vetor C, na qual cada elemento de 
C  é  a  subtração  do  elemento  correspondente  a  A  com  B  ou  B  com  A  para  que  o  valor  da 
subtração fique positivo ou nulo. Ao final, apresentar o vetor C."""
#DETERMINAR VETOR A E B
vet_a = []
vet_b = []

#PERGUNTAR AO USUÁRIO QUANTOS NÚMEROS DESEJA DIGITAR
n = int(input("Quantos números deseja inserir nos vetores? "))

#INSERIR NÚMEROS DENTRO DO VETOR A
print("VETOR A:")
for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    vet_a.append(num)
print()

#INSERIR NÚMEROS DENTRO DO VETOR B
print("VETOR B:")
for i in range(n):
    num = int(input(f"Digite o {i+1}° número: "))
    vet_b.append(num)
print()

#DETERMINAR VETOR C
vet_c = []

#FAZER A SUBTRAÇÃO DO VETOR A E B INSERINDO NO VETOR C
print("VETOR C:")
for i in range(n):
    subtracao = vet_a[i] - vet_b[i]
    vet_c.append(subtracao)
print()

#IMRPRIMIR OS VETORES A, B, C
print(f"VETOR A = {vet_a}")
print(f"VETOR B = {vet_b}")
print(f"VETOR C = {vet_c}")
