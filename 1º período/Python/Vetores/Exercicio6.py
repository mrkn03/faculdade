"""Desenvolva um programa que realize as seguintes tarefas:

1. Leia o nome e duas notas de 10 alunos. 
2. Armazene os nomes em um vetor. 
3. Armazene as duas notas de cada aluno em dois vetores distintos. 
4. Calcule e armazene a média de cada aluno em um terceiro vetor. 
5. Ao final, exiba: 
    • O nome e a média de cada aluno. 
    • O nome do aluno com a maior média. 
    • A quantidade de alunos com média menor que 5. """
#DETERMINAR OS VETORES
vet_nome = []
vet_nota1 = []
vet_nota2 = []
vet_media = []

#PERGUNTAR AO CLIENTE QUANTOS ALUNOS IRÁ DIGITAR
n = int(input("Você ira digitar as notas de quantos alunos? "))

#ARMAZENAR OS NOMES DENTRO DO VETOR
for i in range(n):
    nome = str(input(f"Digite o nome do {i+1}º aluno: "))
    vet_nome.append(nome)

#ARMAZENAR PRIMEIRA NOTA DOS ALUNOS
for i in range(n):
    nota1 = float(input(f"Digite a primeira nota do {i+1}º aluno: "))
    vet_nota1.append(nota1)

#ARMAZENAR SEGUNDA NOTA DOS ALUNOS
for i in range(n):
    nota2 = float(input(f"Digite a segunda nota do {i+1}º aluno: "))
    vet_nota2.append(nota2)

#FAZER A MÉDIA DAS DUAS NOTAS DOS ALUNOS
for i in range(n):
    media = (vet_nota1[i] + vet_nota2[i])/2
    vet_media.append(media)

#NOME E MÉDIA DOS ALUNOS
for i in range(n):
    print(f"{i+1}º aluno: Nome: {vet_nome[i]}, Média: {vet_media[i]}")

#CRIAR INDICE PARA SABER A POSIÇÃO DA MAIOR MÉDIA
maior_media = 0
for i in range(n):
    if vet_media[i] > maior_media:
        maior_media = vet_media[i]
        indice = vet_media.index(maior_media)

#NOME E NOTA DO ALUNO QUE OBTEVE A MAIOR MÉDIA
print(f"A maior média foi a do aluno {vet_nome[indice]} que obteve {maior_media} pontos")

#QUANTIDADE DOS ALUNOS QUE OBTEVE MÉDIA MENOR QUE 5
cont = 0
for i in range(n):
    if vet_media[i] < 5:
        cont += 1

print(f"No total {cont} alunos obtiveram a média menor que 5")