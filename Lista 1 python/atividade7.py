#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.
# Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.
dia = float (input("Insira o dia(1 a 30):"))
mes = float (input("Insira o mês(1 a 12):"))
total = (mes-1) * 30 + dia
#É mês - 1 pq este 1 é o mes em q estamos, a contagem deve ser dos meses que ja passaram
print (f"Se passaram {total} dias desde o início do ano!")


