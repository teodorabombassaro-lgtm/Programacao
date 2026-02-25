#Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma: 
#CENTENA = x
#DEZENA = x 
#UNIDADE = x
numero = (input("Digite um número inteiro de no máximo três digitos: "))
print (f'centena:{numero[:1]}')
print (f'dezena:{numero[1:2]}')
print (f'unidade:{numero[2:]}')