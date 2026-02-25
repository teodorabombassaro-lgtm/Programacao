#Faça um algoritmo para ler três notas de um aluno em uma disciplina 
# imprimir a sua média ponderada (as notas tem pesos respectivos de 1, 2 e 3).
contador = 1
soma_notas = 0
while contador <= 3:
    nota = float (input(f"Inira a {contador} nota do aluno: "))
    if nota <0 or nota >3:
        print ("Nota inválida. A nota deve estar entr 1 e 3.")
        continue
    soma_notas += nota
    contador +=1
media = soma_notas/3
print ("A média das três notas é: ", media)