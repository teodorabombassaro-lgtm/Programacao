#Faça um algoritmo que receba o valor dos catetos de um triângulo e calcule e mostre o valor da hipotenusa.
cateto1 = float (input("Insira a medida do primeiro cateto:"))
cateto2 = float (input("Insira a medida do segundo cateto:"))
soma = (cateto1**2) + (cateto2**2) **0.5
print (f"A medida da hipotenusa é igual a {soma} cm")
