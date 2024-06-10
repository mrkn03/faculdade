"""Leia 10 números pares fornecidos pelo usuário, armazene-os em um vetor A e gere um vetor 
B com o resultado de cada número elevado a 3. O usuário  poderá fornecer qualquer número, 
mas deverão ser considerados apenas os pares."""
#USUÁRIO DECIDE QUANTOS NÚMEROS INSERIR NO VETOR
n = int(input("Quantos números você deseja digitar? "))

#DETERMINAR O VETOR A
vet_a = []

#INSERIR OS NÚMEROS PARES DENTRO DO VETOR A
for i in range(n):
    num = int(input(f"Digite o {i+1}º número par: "))
    if num % 2 != 0:
        num = int(input("Numero impar. Digite novamente "))
    else:
        vet_a.append(num)

#DETERMINAR O VETOR B
vet_b = []

#INSERIR OS NÚMEROS DO VETOR A DENTRO DO VETOR B E ELEVAR A 3
for i in vet_a:
    vet_b.append(vet_a[i]**3)

#IMPRIMIR OS DOIS VETORES
print(f"VETOR A = {vet_a}")
print(f"VETOR B = {vet_b}")