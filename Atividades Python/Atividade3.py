contador = 1
soma_notas = 0
while contador <= 4:
    nota = float(input(f"Inira a nota do {contador} aluno: "))
    if nota <0 or nota >10:
        print ("Nota inválida. A nota deve estar entr 0 e 10.")
        continue
    soma_notas += nota
    contador +=1
media = soma_notas/4
print ("A média das quatro notas é: ", media)