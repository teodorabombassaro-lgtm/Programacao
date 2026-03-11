#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. 
#Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário.
#Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.
hora_normal = float (input("Quantas horas você trabalhou(Não cite horas extra):"))
hora_extra = float (input("Quantas horas extra você trabalhou:"))
salario_bruto = (hora_extra * 15) + (hora_normal * 10)
imposto = salario_bruto * 0.10
salario_liquido = salario_bruto - imposto
print ("O seu salário bruto é de: R$",salario_bruto)
print ("O seu salário liquido é de: R$",salario_liquido)
