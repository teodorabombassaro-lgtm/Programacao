#Calcule o volume de uma caixa d'água cilíndrica.
altura = float (input("Qual a medida em metros altura da caixa d'água?"))
raio = float (input("Qual a medida em metros do raio da caixa d'água?"))
volume = 3.14159 * (raio * 2) * altura
print (f"O volume de uma caixa d'água cilíndrica é de: {volume:.2f} M³")