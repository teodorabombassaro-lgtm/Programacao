#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
#Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, 
#calcule e mostre a comissão e o salário final do funcionário.
salario = float (input("Digite o sálario do vendedor:"))
vendas = float (input("Qual o valor total de suas vendas?"))
comissao = vendas * 0.4
salario_final = salario + comissao
print (f"O valor da comissão que este funcionário recebe é de R${comissao} e o salário final de R${salario_final}")