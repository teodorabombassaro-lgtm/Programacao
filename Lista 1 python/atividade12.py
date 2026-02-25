#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. 
#Após o aumento, desconte 8% de impostos. 
#Imprima o salário inicial, o salário com o aumento e o salário final.
salario = float (input("Digite seu sálario: R$"))
aumento = (salario * 0.15) + salario
imposto = aumento * 0.8
salario_final = aumento - imposto
print ("Salário inicial: R$",salario)
print ("Salário com aumento: R$",aumento)
print ("Salário final: R$",salario_final)
