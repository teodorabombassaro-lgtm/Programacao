#Um tonel de refresco é feito com 8 partes de água mineral e 
#2 partes de suco de maracujá. 
#Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco 
#(informados pelo usuário).
litros_refresco = float (input("Quantos litros de refresco você deseja fazer?"))
litros_agua = litros_refresco * 0.8
litros_suco = litros_refresco * 0.2
total_litros = litros_agua + litros_suco
print(f"Para fazer {litros_refresco} litros de refresco, precisamos de {litros_agua} litros de água e {litros_suco} litros de suco")
