"""Dado um vetor com 20 letras, escreva um algoritmo para: 

a)  contar  quantas  vezes  apareceu  a  letra  "A".  Se  a  letra  "A"  não  estiver  no  vetor,  informe  ao usuário; 
 
b) contar quantas vezes ocorre um mesmo par de letras no vetor e quais são elas. Par de letra é quando letras iguais estão em posições sequenciais."""

#DETERMINAR O VETOR
vet = []

#PEDIR AO USUÁRIO DIGITAR UMA FRASE
frase = str(input("Digite uma frase: ")).split()

#INSERIR A FRASE DIGITADA NO VETOR
for i in frase:
    vet.append(i)
print(vet)