# O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
# Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
# Assuma que a balança já desconte o peso do prato.
quilos = float (input("Insira o peso do prato em quilos: "))
valor = quilos * 12.00
print ("O valor a pagar pela refeição é: R$",valor)