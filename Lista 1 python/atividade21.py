#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: 
#lata de 350 ml, 
#garrafa de 600 ml 
#garrafa de 2 litros. 
#Se um comerciante compra uma determinada quantidade de cada formato, 
#faça um algoritmo para calcular quantos litros de refrigerante ele comprou.
lata = float (input("Quantas latas de 350 ml você comprou?"))
garrafa_600 = float (input("Quantas garrafas de 600 ml você comprou?"))
garrafa_2 = float (input("Quantas grrafas de 2 litos você comprou?"))
total = (lata * 350) + (garrafa_600 * 600) + (garrafa_2 * 2000)
print (f"Você comprou um total de {total} ml de refrigerante")