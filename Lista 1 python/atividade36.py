#Faça um algoritmo que receba o valor do salário mínimo e o valor do salário de um funcionário
#calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.
sal_minimo = float(input("Valor do salário mínimo: R$ "))
sal_func = float(input("Salário do funcionário: R$ "))

quantidade = sal_func / sal_minimo

print(f"O funcionário ganha o equivalente a {quantidade:.2f} salários mínimos.")

