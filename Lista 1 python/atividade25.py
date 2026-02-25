#Calcule o volume de uma caixa d'água cilíndrica.
altura = float (input("Qual a medida em metros altura da caixa d'água?"))
raio = float (input("Qual a medida em metros do raio da caixa d'água?"))
conta = (3.14 * raio ** 2) * altura
volume = conta * 1000
print (f"O volume de uma caixa d'água cilíndrica é de: {volume} litros")