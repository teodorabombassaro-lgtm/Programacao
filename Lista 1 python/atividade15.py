#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. 
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, 
#Faça com que Carlos e André não paguem centavos. 
#Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para Felipe.
total = float(input("Qual foi o valor total da conta?"))
valor_por_pessoa = total / 3
#(int) o valo_por_pessoa vai virar inteiro e remover a virgula (ex: 10,56 = 10)

carlos = int(valor_por_pessoa)
andre = int(valor_por_pessoa)
felipe = total - (carlos + andre)
print ("Carlos deve pagar R$ {:.2f}". format (carlos))
print ("André deve pagar R$ {:.2f}". format (andre))
print ("Felipe deve pagar R$ {:.2f}". format (felipe))

#{:.2f}". format (variavel). ISso é usadopara permitir apenas duas casas(numeros) apos a vírgula. ex: 33,5555 = 33,55
