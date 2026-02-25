#Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. 
#Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias.
dias_trabalhados = int (input("Quantos dias você trabalou sem acidentes?"))
anos = dias_trabalhados // 365
meses = (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) % 30
print (f"Você já trabalhou {anos} anos, {meses} meses e {dias} dias!")
# a % é útil pra quando é necessário resgatar a sobra de uma divisão para usá-la posteriormente