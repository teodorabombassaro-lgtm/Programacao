# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. 
# Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda
# A máquina informa quanto será o valor arrecadado.
quantidade_pequenas = int (input("Insira a quantidade de camisetas pequenas referentes a venda: "))
quantidade_medias = int (input("Insira a quantidade de camisetas médias referentes a venda: "))
quantidade_grandes = int (input("Insira a quantidade de camisetas grandes referentes a venda: "))
print ("O valor total arrecadado é de: R$ ",(quantidade_pequenas*10) + (quantidade_medias*12) + (quantidade_grandes*15))
#Uma forma simples e util é fazer a conta ao final no print, isso pode diminuir  quantidade de variaveis
