"""Preencha um vetor de 5 posições com valores inteiros. Calcule a média ponderada dos
valores que estão no vetor. Essa média é a soma de cada elemento multiplicada pela sua
posição no vetor e, em seguida, dividido pela quantidade de elementos."""
#DETERMINAR VETOR
vet_a = []

#PREENCHER VETOR
for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)


#FAZER A SOMA DOS ELEMENTOS DO VETOR PELA SUA POSIÇÃO
soma = 0
for i in range(5):
    soma += vet_a[i] * (i+1)

#FAZER A MÉDIA DA SOMA DO VETOR
media = soma / 5

#IMPRIMIR O VETOR E SUA MÉDIA PONDERADA
print(f"Vetor A = {vet_a}")
print(f"Média ponderada do vetor A = {media}")