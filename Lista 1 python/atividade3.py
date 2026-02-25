# A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. 
# Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos)
# Quanto deve guardar numa conta de poupança (10% do total arrecadado).
pao = int (input("Quantos pães foram vendidos hoje?"))
broa = int (input("Quantas broas foram vendidas hoje?"))
total = (pao * 0.12) + (broa * 1.50)
poupanca = total * 0.10
print ("O total de pães e broas arrecadados juntos foi de R$",total)
print ("A quantidade que deve ser guardada na poupança é de R$",poupanca)
#Tambem é possivel fazer de outra forma as linhas 8 e 10, diminuindo assim uma variavel
# Exemplo: print("A quantidade...", total * 0.10)