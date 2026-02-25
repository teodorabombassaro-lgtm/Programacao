#Faça um algoritmo que receba o preço de um produto,
#calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
preco = float (input("Qual o preço do produto?"))
desconto = preco * 0.10
preco_final = preco - desconto
print ("Com um desconto de 10% aplicado o valor final a pagar pelo produto é de: R$", preco_final)