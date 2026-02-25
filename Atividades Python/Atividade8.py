#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
h = float(input("Insira sua altura"))
sexo = (input("Insira o seu gênero (F para feminino e M para masculino)"))
if sexo == "M":
    peso_ideal =(72.7*h) - 58
    print ("O peso ideal masculino com sua altura é:",peso_ideal)
elif sexo == "F":
    peso_ideal = (62.1 * h) - 44.7
    print ("O peso ideal feminino de acordo com sua altura é:",peso_ideal)
else:
    print("Sexo inválido, por favor insira M para masculino ou F para feminino") 