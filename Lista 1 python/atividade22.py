#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
#Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. 
#Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. 
#Não havendo moeda de um tipo, a quantidade respectiva é zero.
moeda_1 = float (input("Digite a quantidade de moedas de 1 real que você tem:"))
moeda_01 = float (input("Digite a quantidade de moedas de 0.01 centavos que você tem:"))
moeda_5 = float (input("Digite a quantidade de moedas de 0.05 centavos que você tem:"))
moeda_10 = float (input("Digite a quantidade de moedas de 0.10 centavos que você tem:"))
moeda_25 = float (input("Digite a quantidade de moedas de 0.25 centavos que você tem:"))
moeda_50 = float (input("Digite a quantidade de moedas de 0.50 centavos que você tem:"))
total = moeda_01 + moeda_5 + moeda_10 + moeda_25 + moeda_50 + moeda_1
print ("A quantidade em reais economizada é de: RS", total)