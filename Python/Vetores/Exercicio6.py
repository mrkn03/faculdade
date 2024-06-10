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
vet_nota = []

#ARMAZENAR OS NOMES DENTRO DO VETOR
for i in range(0,2):
    nome = str(input(f"Digite o nome do {i+1}º aluno: "))
    vet_nome.append(nome)

#ARMAZENAR AS NOTAS DOS ALUNOS
