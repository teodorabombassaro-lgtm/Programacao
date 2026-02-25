#Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
#o novo peso se a pessoa engordar 15% sobre o peso digitado;
#o novo peso se a pessoa emagrecer 20% sobre o peso digitado.
peso = float (input("Digite o seu peso:"))
engordar = peso * 0.15
final_peso_maior = peso + engordar 
emagrecer = peso * 0.20
final_peso_menor = peso - emagrecer
print (f"O seu peso caso engordasse 15% em relação ao seu peso atual seria:{final_peso_maior}")
print (f"O seu peso caso emagrecesse 20% em relação ao seu peso atual seria:{final_peso_menor}")