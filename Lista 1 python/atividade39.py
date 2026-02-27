#João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas 
#(C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. 
#Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. 
#Faça um algoritmo que calcule e mostre quanto restará do salário do João
salario = 1200.00
multa_C1 = (200.00 * 0.2) + 200.00
multa_C2 = (120.00 * 0.2) + 120.00
sobra_do_salario = salario - (multa_C1 + multa_C2)
print ("O que sobrará do salário de João após pagar as contas é: R${:.2f}". format (sobra_do_salario))

