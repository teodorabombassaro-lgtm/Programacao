#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui.
# Considere sempre anos completos, e que um ano possui 365 dias.
# Ex: uma pessoa com 19 anos possui 6935 dias de vida
# Ex: veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS
nome=input("Digite o seu nome: ")
idade=float (input("Digite a sua idade: "))
dias=idade*365
print(f"{nome}, você ja viveu {dias} dias")
#Lembrar sempre de adicionar {} e F para adicionar variáveis no meio da frase do print