#Faça um algoritmo que receba dois números, 
#calcule e mostre a divisão do primeiro número pelo segundo. 
#Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.
numero1 = float (input("Insira o primeiro número:"))
numero2 = float (input("Insira o segundo número(obrigatóriamente diferente de 0):"))
total = numero1 / numero2
print (f"O total da conta {numero1} / {numero2} é {total}")
